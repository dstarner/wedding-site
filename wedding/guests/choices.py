from django.db import models


class PartyType(models.TextChoices):

    INDIVIDUAL = '& Guest', 'Individual with Guest'
    COUPLE = 'Couple', 'Couple with Two Known Guests'
    FAMILY = 'Family', 'Family with Kids'


class IndividualAssociation(models.TextChoices):
    """Which side of the family are they associated with 
    """
    BRIDGET = 'bridge', 'Bridget'
    DAN = 'dan', 'Dan'


class AssociationType(models.TextChoices):
    """How does the person / family know them?
    """
    FAMILY = 'family', 'Family'
    FRIEND = 'friend', 'Friends'
    WORK = 'work', 'Work Colleague'
    FAMILY_FRIEND = 'fam_friend', 'Family Friend'


class PriorityTier(models.IntegerChoices):
    """How important is it for them to be at the wedding?
    """
    WEDDING_PARTY = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    FALLBACK = 4


class PreferredContactMethod(models.TextChoices):
    """How should we contact the party?
    """
    EMAIL = 'email' 'Email'
    PHONE = 'phone', 'Phone (Texting)'
    MAIL = 'mail', 'Postal Mail'


class Role(models.TextChoices):

    BEST_MAN = 'best_man', 'Best Man'
    MAID_OF_HONOR = 'maid_of_honor', 'Maid of Honor'

    GROOMSMAN = 'groomsman', 'Groomsman'
    BRIDESMAID = 'bridesmaid', 'Bridesmaid'
    