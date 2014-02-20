from django.test import TestCase
import datetime
from django.utils.timezone import utc
from plns.payments.models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(name = 'Woody',amount=300, pricePerUnit=3.15, data = datetime.datetime(2003, 12, 3, 10, 18, 30, tzinfo=utc))
        Payment.objects.create(name = 'Buzz',amount=-300, pricePerUnit=-4.15, data = datetime.datetime(2008, 3, 12, 11, 8, 9, tzinfo=utc), weight=300)
        Payment.objects.create(name = 'MrPotato',amount=300, pricePerUnit=5, data = datetime.datetime(2007, 5, 10, 10, 1, 5, tzinfo=utc), weight=-300)
    def test_price_is_bigger_than_zero(self):
        """Check if price is correct"""
        paymentFirst = Payment.objects.get(name='Woody')
        paymentSecond = Payment.objects.get(name='Buzz')
        self.assertGreater(paymentFirst.pricePerUnit, 0)
        self.assertGreater(paymentSecond.pricePerUnit, 0)

    def test_amount_is_bigger_than_zero(self):
        """Check if amount is correct"""
        paymentFirst = Payment.objects.get(name='Woody')
        paymentSecond = Payment.objects.get(name='Buzz')
        self.assertGreater(paymentFirst.amount, 0)
        self.assertGreater(paymentSecond.amount, 0)

    def test_weight_is_bigger_than_zero(self):
        """Check if price is correct"""
        paymentFirst = Payment.objects.get(name='Woody')
        paymentSecond = Payment.objects.get(name='Buzz')
        if not paymentFirst.weight is None:
            self.assertGreater(paymentFirst.pricePerUnit, 0)
        if not paymentSecond.weight is None:
            self.assertGreater(paymentSecond.pricePerUnit, 0)
