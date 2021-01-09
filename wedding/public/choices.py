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