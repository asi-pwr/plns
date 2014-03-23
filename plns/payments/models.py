from django.db import models
from django.utils.translation import ugettext as _
from mptt.models import MPTTModel, TreeForeignKey
from plns.users.models import User

class PaymentManager(models.Manager):
    def date_sort(self, date_start, date_end):
        return self.filter(timestamp__range=(date_start, date_end))

    def amount_sort(self, amount_start, amount_end):
        return self.filter(amount__range=(amount_start, amount_end))

class Payment(models.Model):
    name = models.TextField(_('Name'))
    timestamp = models.DateTimeField(_('Date and Time'))
    amount = models.FloatField(_('Amount'))
    price_per_unit = models.FloatField(_('Price per unit'))
    weight = models.FloatField(_('Weight'), blank=True, default=None, null=True)

class Category(MPTTModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    parent = TreeForeignKey('self', null=True, blank=True,
				 related_name='children')


    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

