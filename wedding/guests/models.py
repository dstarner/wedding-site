import os.path
import random, string

from address.models import AddressField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .choices import (
    AssociationType, IndividualAssociation, PreferredContactMethod, PartyType, PriorityTier, Role
)


class Party(models.Model):

    name = models.CharField(
        'Name',
        max_length=64, default='', help_text='First & last of main party member'
    )

    phone = PhoneNumberField(
        blank=True, null=True,
        help_text='Phone number to contact main party individual, if available.'
    )
    address = AddressField(
        blank=True, null=True,
        help_text='Address of the main party individual, if available.'
    )
    second_address = models.CharField(
        'Second Address', max_length=64, null=True, blank=True, help_text='Apartment Number if needed'
    )

    contact_method = models.CharField(
        'Preferred Contact Method',
        max_length=16, default=PreferredContactMethod.MAIL, choices=PreferredContactMethod.choices
    )

    type = models.CharField(
        'Party Type',
        max_length=32, choices=PartyType.choices, default=PartyType.INDIVIDUAL,
        help_text='Defines the party type and will automatically suffix correctly'
    )
    tier = models.IntegerField('Priority Tier', choices=PriorityTier.choices, default=PriorityTier.HIGH)
    association = models.CharField('Association', max_length=16, choices=AssociationType.choices, default=AssociationType.FRIEND)
    side = models.CharField('Wedding Side', max_length=8, choices=IndividualAssociation.choices)

    is_invited = models.BooleanField(default=False, help_text='Whether or not the party is actually invited.')
    guests_allowed = models.IntegerField('Max Guests Allowed', default=2, help_text='How many people should we expect')
    rehearsal_dinner = models.BooleanField(
        default=False, help_text='Whether the party is invited to the rehearsal dinner'
    )

    save_the_date_sent = models.BooleanField(default=False)
    invitation_sent = models.BooleanField(default=False)
    rsvped = models.BooleanField(default=False)
    attending = models.IntegerField('# Attending', default=0)
    comments = models.TextField(null=True, blank=True)

    code = models.CharField('Party Code', editable=False, unique=True, max_length=4, default='', help_text='Unique code that identifies the party')

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ['tier']

    def save(self, *args, **kwargs):
        if self.tier == PriorityTier.WEDDING_PARTY:
            self.rehearsal_dinner = True
        # TODO: check if not self.is_invited but invite / std was sent:

        if self.attending > 0:
            self.rsvped = True

        if self.code == '':
            self.code = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        res = super().save(*args, **kwargs)

        if self.guests.count() == 0 and len(self.name.split(' ')) == 2:
            first_name, last_name = self.name.split(' ')
            Guest.objects.create(
                first_name=first_name, party=self,
                last_name=last_name,
                phone=self.phone
            )

    @property
    def full_name(self):
        return f'{self.name} {self.type}'

    def __str__(self):
        guests_saved = self.guests.count()
        suffix = f' - {guests_saved}'
        if guests_saved != self.guests_allowed:
            suffix = f' - {guests_saved} of {self.guests_allowed}'
        return f'{self.name} {suffix}'


def guest_picture_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'guests/pictures/{instance.last_name}_{instance.first_name}{extension}'


class MealChoices(models.TextChoices):

    CHICKEN = 'chicken', 'Chicken'
    STEAK = 'steak', 'steak'
    VEGGIE = 'vegetarian', 'Vegetarian Pasta'


class Guest(models.Model):

    party = models.ForeignKey(Party, on_delete=models.PROTECT)

    first_name = models.CharField('First Name', max_length=64)
    last_name = models.CharField('Last Name', max_length=64)

    meal = models.CharField(null=True, blank=True, choices=MealChoices.choices, max_length=12)

    requests = models.TextField(default='', help_text='Allergies and special requests')

    phone = PhoneNumberField(blank=True, null=True, help_text='Needs "+1" and then 10 digit, ie +17165554444')

    role = models.CharField('Wedding Role', max_length=16, blank=True, null=True, choices=Role.choices)
    is_child = models.BooleanField(default=False)

    picture = models.ImageField(
        null=True, blank=True, upload_to=guest_picture_path,
        help_text='Needed if they are in the wedding party'
    )

    class Meta:
        ordering = ['party', 'id']
        default_related_name = 'guests'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __getattr__(self, attr):
        return getattr(self.party, attr)

    def __str__(self):
        return f'Guest: {self.name}'


