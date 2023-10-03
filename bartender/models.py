from django.db import models


class BarTender(models.Model):
    name = models.CharField(max_length=200, unique=True)
    experience_years = models.PositiveIntegerField()
    drinks = models.ManyToManyField('drinks.Drink', related_name='bartenders', blank=True)
