import os.path

from address.models import AddressField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .choices import AssociationType, IndividualAssociation, PreferredContactMethod, PriorityTier, Role


class Party(models.Model):

    name = models.CharField(
        'Name',
        max_length=64, default='Mr & Mrs', help_text='Easy way to reference party'
    )

    email = models.EmailField(
        'Primary Email',
        help_text='Email to contact main party individual, if available.', blank=True, null=True
    )
    phone = PhoneNumberField(
        blank=True, null=True,
        help_text='Phone number to contact main party individual, if available.'
    )
    address = AddressField(
        blank=True, null=True,
        help_text='Address of the main party individual, if available.'
    )

    contact_method = models.CharField(
        'Preferred Contact Method',
        max_length=16, default=PreferredContactMethod.MAIL, choices=PreferredContactMethod.choices
    )

    tier = models.IntegerField('Priority Tier', choices=PriorityTier.choices)
    association = models.CharField('Association', max_length=16, choices=AssociationType.choices)
    side = models.CharField('Wedding Side', max_length=8, choices=IndividualAssociation.choices)

    is_invited = models.BooleanField(default=False, help_text='Whether or not the party is actually invited.')
    guests_allowed = models.IntegerField('Max Guests Allowed', default=2, help_text='How many people should we expect')
    rehearsal_dinner = models.BooleanField(
        default=False, help_text='Whether the party is invited to the rehearsal dinner'
    )

    is_attending = models.BooleanField(null=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ['tier']

    def save(self, *args, **kwargs):
        if self.tier == PriorityTier.WEDDING_PARTY:
            self.rehearsal_dinner = True
        # TODO: check if not self.is_invited but invite / std was sent:
        return super().save(*args, **kwargs)

    def __str__(self):
        guests_saved = self.guests.count()
        suffix = ''
        if guests_saved != self.guests_allowed:
            suffix = f' (of {self.guests_allowed})'
        return f'{self.name} Party of {guests_saved if guests_saved else self.guests_allowed}{suffix}'


def guest_picture_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f'guests/pictures/{instance.last_name}_{instance.first_name}{extension}'


class Guest(models.Model):

    party = models.ForeignKey(Party, on_delete=models.PROTECT)

    first_name = models.CharField('First Name', max_length=64)
    last_name = models.CharField('Last Name', max_length=64)

    email = models.EmailField('Email', blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True, help_text='Needs "+1" and then 10 digit, ie +17165554444')

    role = models.CharField('Wedding Role', max_length=16, blank=True, null=True, choices=Role.choices)
    is_child = models.BooleanField(default=False)

    picture = models.ImageField(
        null=True, blank=True, upload_to=guest_picture_path,
        help_text='Needed if they are in the wedding party'
    )
    details = models.TextField(blank=True, default='', help_text='Needed only if they are in the wedding party.')

    class Meta:
        ordering = ['party', 'last_name']
        default_related_name = 'guests'
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Guest: {self.name}'

