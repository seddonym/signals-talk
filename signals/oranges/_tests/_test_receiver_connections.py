"""WARNING: Do not import or patch anything from oranges.receivers in this file,
otherwise this the .
"""
from unittest import TestCase, skip
from unittest.mock import patch
from apples.models import Apple, Pippin
from apples.signals import apple_eaten
from django.db.models import signals


class ReceiverConnectionTestCase(TestCase):
    def assert_receiver_is_connected(self, receiver_string, signal, sender):
        receivers = signal._live_receivers(sender)
        receiver_strings = ["{}.{}".format(r.__module__, r.__name__) for r in receivers]
        if receiver_string not in receiver_strings:
            raise AssertionError('{} is not connected to signal.'.format(receiver_string))


class TestConnection(ReceiverConnectionTestCase):
    """Unit tests for receivers.
    """
    def test_pippin_eaten_receiver(self):
        self.assert_receiver_is_connected('oranges.receivers.pippin_eaten_receiver', apple_eaten, Pippin)
