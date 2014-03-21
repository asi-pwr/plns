
import collections
import datetime
import itertools
import operator
from django.utils.translation import ugettext as _
from plns.payments.models import  Payment


def date_range(date_from, date_to):
    days = (date_to - date_from).days + 1
    for date in (date_from + datetime.timedelta(d) for d in xrange(days)):
        yield date


class Chart(object):
    name = ''
    template_name = ''
    group_by = ''
    aggregation_func = None

    def __init__(self, width=1024, height=500):
        self.width = width
        self.height = height

        if not self.name:
            raise AttributeError('Invalid title')
        self.id = self.name.strip().lower().replace(' ', '-')

    def get_date_range(self):
        raise NotImplementedError('get_date_range')

