from django.dispatch import receiver
from apples.signals import apple_eaten
from apples.models import Bramley, Pippin, RottenApple
from .utils import handle_pippin_eaten


@receiver(apple_eaten)
def apple_eaten_receiver(sender, bites, **kwargs):
    print("Apple eaten in {} bites.".format(bites))


@receiver(apple_eaten, sender=Bramley)
def bramley_eaten_receiver(sender, bites, **kwargs):
    print("Bramley eaten in {} bites.".format(bites))


@receiver(apple_eaten, sender=Pippin)
def pippin_eaten_receiver(sender, bites, **kwargs):
    handle_pippin_eaten(bites=bites)


@receiver(apple_eaten, sender=RottenApple)
def dodgy_receiver(sender, bites, **kwargs):
    raise RuntimeError('Something dodgy happened.')


def connect_local_receivers():
    # Both of these inner functions will be garbage collected, by default.
    def local_receiver_incorrect(sender, bites, **kwargs):
        print("Locally eaten (this won't work).")
    
    def local_receiver_correct(sender, bites, **kwargs):
        print('Locally eaten.')
    
    apple_eaten.connect(local_receiver_incorrect)
    apple_eaten.connect(local_receiver_correct, weak=False)

connect_local_receivers()
