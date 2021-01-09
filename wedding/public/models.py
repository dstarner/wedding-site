from io import BytesIO
from mimetypes import guess_type
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from PIL import Image

from .choices import MonthChoices


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
    thumbnail_image_field.save(
        image_field.name,
        InMemoryUploadedFile(
            image_file,
            None, '',
            guess_type(image_field.file.name),
            image.size,
            'utf-8',
        ),
        save=False
    )


class TimelineEntry(models.Model):

    title = models.CharField('Entry Title', max_length=32)

    month = models.IntegerField('Month', choices=MonthChoices.choices, help_text='Abbreviation for the month to show')

    year = models.IntegerField(
        help_text='Can be between 2013 and 2022',
        validators=[MinValueValidator(2013), MaxValueValidator(2022)]
    )

    details = models.TextField()

    picture = models.ImageField(upload_to=entry_picture_path)

    class Meta:
        ordering = ('year', 'month')
        verbose_name_plural = 'Timeline Entries'


class GalleryItem(models.Model):

    title = models.CharField('Title', max_length=64)

    picture = models.ImageField(upload_to=gallery_picture_path)

    thumbnail = models.ImageField(null=True, blank=True, upload_to=gallery_thumbnail_path)

    def save(self, *args, **kwargs):
        _create_thumbnail(self.picture, self.thumbnail, (300, 300))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Gallery Items'


class RegistryOrganization(models.Model):

    details = models.CharField(max_length=128)

    picture = models.ImageField(upload_to=registry_thumbnail_path)

    link = models.URLField(help_text='Link to redirect clicks to')

    class Meta:
        verbose_name_plural = 'Registry Organizations'
