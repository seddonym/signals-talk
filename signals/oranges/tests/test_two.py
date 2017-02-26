from django.test import TestCase
from apples.signals import apple_eaten
from apples.models import Apple

class MyOtherTestCase(TestCase):
    def test_one(self):
        print(apple_eaten._live_receivers(Apple))
    