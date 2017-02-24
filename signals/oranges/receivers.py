from django.dispatch import receiver
from apples.signals import my_signal


@receiver(my_signal)
def my_receiver(sender, foo, bar, **kwargs):
    print("Received with foo='{foo}' and bar='{bar}'.".format(foo=foo, bar=bar))
