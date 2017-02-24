from django.dispatch import receiver
from apples.signals import apple_eaten
from apples.models import Bramley


@receiver(apple_eaten)
def apple_eaten_receiver(sender, bites, **kwargs):
    print("Apple eaten in {} bite(s).".format(bites))


@receiver(apple_eaten, sender=Bramley)
def bramley_eaten_receiver(sender, bites, **kwargs):
    print("Bramley eaten in {} bite(s).".format(bites))
