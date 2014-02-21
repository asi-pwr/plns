from django.test import TestCase
import datetime
from django.utils.timezone import utc
from plns.payments.models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(name = 'Woody',amount=300, price_per_unit=3.15, timestamp = datetime.datetime(2003, 12, 3, 10, 18, 30, tzinfo=utc))
        Payment.objects.create(name = 'Buzz',amount=-300, price_per_unit=-4.15, timestamp = datetime.datetime(2008, 3, 12, 11, 8, 9, tzinfo=utc), weight=300)
        Payment.objects.create(name = 'MrPotato',amount=300, price_per_unit=5, timestamp = datetime.datetime(2007, 5, 10, 10, 1, 5, tzinfo=utc), weight=-300)
