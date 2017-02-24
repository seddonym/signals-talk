from django.dispatch import Signal


# Signal sent when an apple is eaten
apple_eaten = Signal(providing_args=['bites'])
