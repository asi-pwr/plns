from django.db import models
from django.utils.translation import ugettext as _


class Chart(models.Model):
    TYPES = ()
    name = models.CharField(_('Title'), max_length=300)
    config = models.TextField(_('Configuration String'))
    user = models.ForeignKey("users.User", verbose_name=_('User'))
    position = models.IntegerField(_('Position'))
    type = models.IntegerField(choices=TYPES)

    def __unicode__(self):
        return self.name