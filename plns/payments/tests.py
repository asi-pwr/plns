from django.test import TestCase
import datetime
from plns.payments.models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create( name = 'Woody',amount=300, pricePerUnit=3.15)
        Payment.objects.create( name = 'Buzz',amount=300, pricePerUnit=-4.15)
    def test_price_is_zero_or_bigger(self):
        """Check if price is correct"""
        paymentFirst = Payment.objects.get(name='Woody')
        paymentSecond = Payment.objects.get(name='Buzz')
        self.assertGreater(paymentFirst.pricePerUnit, 0)
        self.assertGreater(paymentSecond.pricePerUnit, 0)
