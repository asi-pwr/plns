from django.test import TestCase
import datetime
from django.utils.timezone import utc
from plns.payments.models import Payment
from plns.payments.models import Category
from plns.users.models import User

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(name = 'Woody',amount=300, price_per_unit=3.15, timestamp = datetime.datetime(2003, 12, 3, 10, 18, 30, tzinfo=utc))
        Payment.objects.create(name = 'Buzz',amount=-300, price_per_unit=-4.15, timestamp = datetime.datetime(2008, 3, 12, 11, 8, 9, tzinfo=utc), weight=300)
        Payment.objects.create(name = 'MrPotato',amount=300, price_per_unit=5, timestamp = datetime.datetime(2007, 5, 10, 10, 1, 5, tzinfo=utc), weight=-300)



# Category tests

class CategoryTestCase(TestCase):
    def setUp(self):
        user=User.objects.create_user("example"
					"example@example.com",
					"example")
        self.name = 'first_one'
        self.user=user


    def test_can_create_category(self):
        testcategory = Category.objects.create(name=self.name, user=self.user)
        self.assertTrue(Category.objects.filter(name=self.name).exists())





