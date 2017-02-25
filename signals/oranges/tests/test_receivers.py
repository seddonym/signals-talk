from unittest import TestCase, skip
from unittest.mock import patch
from apples.models import Apple, Pippin, RottenApple
from apples.signals import apple_eaten
from django.db.models import signals
# Never include receivers here


class TestReceivers(TestCase):
    """Unit tests for receivers.
    """
        
    @skip
    def test_apple_eaten_receiver_connection(self):
        # This approach (patching the receiver function) doesn't work.
        with patch('oranges.receivers.apple_eaten_receiver') as mock_receiver:
            apple_eaten.send(Apple, bites=6)
         
        mock_receiver.assert_called_once_with(sender=None, bites=6)
     
    def test_pippin_eaten_delegate(self):
        # This is problematic, because this includes the receivers while we mock it
        # If the receiver delegates most of the behaviour elsewhere, easier to test.
        with patch('oranges.receivers.handle_pippin_eaten') as mock_handle:
            apple_eaten.send(Pippin, bites=5)
           
        mock_handle.assert_called_once_with(bites=5)
        
    def test_disconnection(self):
        # If a particular signal is getting in your way in a test, you can simple disconnect and reconnect
        from oranges.receivers import dodgy_receiver
        apple_eaten.disconnect(dodgy_receiver, sender=RottenApple)
        
        apple_eaten.send(RottenApple, bites=5)
        
        apple_eaten.connect(dodgy_receiver, sender=RottenApple)

        
    def test_mute_signals(self):
        # Todo
        