from django.db import models


class MonthChoices(models.IntegerChoices):

    JAN = 1, 'Jan'
    FEB = 2, 'Feb'
    MAR = 3, 'Mar'
    APR = 4, 'Apr'
    MAY = 5, 'May'
    JUN = 6, 'Jun'
    JUL = 7, 'Jul'
    AUG = 8, 'Aug'
    SEP = 9, 'Sep'
    OCT = 10, 'Oct'
    NOV = 11, 'Nov'
    DEC = 12, 'Dec'


class PlaceChoices(models.TextChoices):

    CEREMONY = 'heart-1', 'Ceremony'
    RECEPTION = 'wine', 'Reception'

    AIRPORT = 'plane', 'Airport'
    PARK = 'tree', 'Parks and Greenspace'
    ATTRACTION = 'star', 'Tourist Attraction'

    @classmethod
    def color(cls, value):
        return {
            cls.AIRPORT: '#797ee6',
            cls.PARK: '#bfd730',
            cls.ATTRACTION: '#e9c24c',
        }.get(value, '#f98d8a')
        


