from django.db import models
import datetime

class Payment(models.Model):
    name = models.TextField('Name')
    amount = models.FloatField('Amount')
    pricePerUnit = models.FloatField('Price per unit')
    weight = models.FloatField('Weight', blank=True, default=None, null=True)
    
