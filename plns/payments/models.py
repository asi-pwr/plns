from django.db import models
from django.utils.translation import ugettext as _

class Payment(models.Model):
    name = models.TextField(_('Name'))
    timestamp = models.DateTimeField(_('Date and Time'))
    amount = models.FloatField(_('Amount'))
    price_per_unit = models.FloatField(_('Price per unit'))
    weight = models.FloatField(_('Weight'), blank=True, default=None, null=True)
    
