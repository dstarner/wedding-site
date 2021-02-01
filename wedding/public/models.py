from io import BytesIO
from mimetypes import guess_type
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from PIL import Image

from .choices import MonthChoices, PlaceChoices


def entry_picture_path(instance, filename):
    return f'timeline/pictures/{filename}'

def gallery_picture_path(instance, filename):
    return f'gallery/pictures/{filename}'

def gallery_thumbnail_path(instance, filename):
    return f'gallery/thumbnail/{filename}'

def registry_thumbnail_path(instance, filename):
    return f'registry/thumbnail/{filename}'


def _create_thumbnail(image_field: ImageFieldFile, thumbnail_image_field: ImageFieldFile, size: tuple):
    image = Image.open(image_field.file.file)
    image.thumbnail(size=size)
    image_file = BytesIO()
    image.save(image_file, image.format)

    mimetype = guess_type(image_field.file.name)
    if mimetype is not None and not isinstance(mimetype, str):
        mimetype = mimetype[0]

    thumbnail_image_field.save(
        image_field.name,
        InMemoryUploadedFile(
            image_file,
            None, '',
            size=image.size,
            content_type=mimetype,
            charset='utf-8',
        ),
        save=False
    )


class PlaceOfInterest(models.Model):

    name = models.CharField(max_length=32)

    link = models.URLField()

    icon = models.CharField(max_length=32, choices=PlaceChoices.choices)

    details = models.TextField()

    lat = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text='Use <a href="https://www.latlong.net/convert-address-to-lat-long.html" target="_blank">this</a> to get values'
    )

    long = models.DecimalField(
        max_digits=9, decimal_places=6,
        help_text='Use <a href="https://www.latlong.net/convert-address-to-lat-long.html" target="_blank">this</a> to get values'
    )

    @property
    def color(self):
        return PlaceChoices.color(self.icon)

    @property
    def type(self):
        return self.get_icon_display().lower().replace(' ', '-')

    @property
    def open_on_load(self):
        return self.icon == PlaceChoices.CEREMONY

    def as_data(self):
        keys = ['name', 'link', 'icon', 'details', 'color', 'type', 'open_on_load', 'lat', 'long']
        data = {}
        for key in keys:
            data[key] = getattr(self, key)
        return data

    def __str__(self):
        return self.name


class TimelineEntry(models.Model):

    title = models.CharField('Entry Title', max_length=32)

    month = models.IntegerField('Month', choices=MonthChoices.choices, help_text='Abbreviation for the month to show')

    year = models.IntegerField(
        help_text='Can be between 2010 and 2022',
        validators=[MinValueValidator(2010), MaxValueValidator(2022)]
    )

    details = models.TextField()

    picture = models.ImageField(upload_to=entry_picture_path)

    class Meta:
        ordering = ('year', 'month')
        verbose_name_plural = 'Timeline Entries'

    def __str__(self):
        return self.title


class GalleryItem(models.Model):

    title = models.CharField('Title', max_length=64)

    picture = models.ImageField(upload_to=gallery_picture_path)

    thumbnail = models.ImageField(null=True, blank=True, upload_to=gallery_thumbnail_path)

    def save(self, *args, **kwargs):
        _create_thumbnail(image_field=self.picture, thumbnail_image_field=self.thumbnail, size=(300, 300))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gallery Items'


class RegistryOrganization(models.Model):

    title = models.CharField(max_length=32, default='')

    picture = models.ImageField(upload_to=registry_thumbnail_path)

    link = models.URLField(help_text='Link to redirect clicks to')

    details = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Registry Organizations'
