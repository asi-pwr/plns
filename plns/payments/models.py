from django.db import models

class Payment(models.Model)
    name = models.TextField('Name')
    timestamp = models.DateTimeField('Date and Time:')
    amount = models.FloatField('Amount')
    price_per_unit = models.FloatField('Price per unit')
    weight = models.FloatField('Weight', blank=True, default=None, null=True)
    
