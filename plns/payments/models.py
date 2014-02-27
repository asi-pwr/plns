from django.db import models
from django.utils.translation import ugettext as _
from mptt.models import MPTTModel, TreeForeignKey

class Payment(models.Model):
    name = models.TextField(_('Name'))
    timestamp = models.DateTimeField(_('Date and Time'))
    amount = models.FloatField(_('Amount'))
    price_per_unit = models.FloatField(_('Price per unit'))
    weight = models.FloatField(_('Weight'), blank=True, default=None, null=True)
    
class Category(MPTTModel):
    name = models.CharField(max_length=50)
   # user = models.ForeignKey(User)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

