from .signals import apple_eaten


class Apple:
    def eat(self):
        """Eats the apple.
        """
        # Dispatch signal
        apple_eaten.send(self.__class__, bites=1)
        

class Bramley(Apple):
    pass


class Pippin(Apple):
    pass
