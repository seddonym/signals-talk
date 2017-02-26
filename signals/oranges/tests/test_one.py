from unittest import TestCase, mock
import sys
from apples.signals import apple_eaten
from apples.models import Apple


class MyTestCase(TestCase):
    def test_one(self):
        with mock.patch('oranges.receivers.handle_pippin_eaten'):
            print(apple_eaten._live_receivers(Apple))
    
    def test_two(self):
        print(apple_eaten._live_receivers(Apple))