from .signals import apple_eaten


class Apple:
    def eat(self):
        """Eats the apple.
        """
        # Dispatch signal
        apple_eaten.send(self.__class__, bites=1)
            
    def eat_carefully(self):
        """Eats the apple carefully.
        """
        # Send the signal, but handle any exceptions one by one
        results = apple_eaten.send_robust(self.__class__, bites=1)
        errors = False
        for receiver, exception in results:
            if exception:
                print('{} raised in receiver {}: "{}"'.format(exception.__class__.__name__, receiver.__name__, exception))
                errors = True
        if not errors:
            print('Everything went fine.')
         

class Bramley(Apple):
    pass


class Pippin(Apple):
    pass


class RottenApple(Apple):
    pass
