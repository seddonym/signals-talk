from django.apps import AppConfig as BaseAppConfig
from django.utils.module_loading import autodiscover_modules
from apples.signals import apple_eaten
from apples.models import Apple

class AppConfig(BaseAppConfig):
    name = 'main'

    def ready(self):
        # Automatically import all receivers files
        #autodiscover_modules('receivers')
        #from oranges import receivers
        from datetime import datetime
        print('Hello {}'.format(datetime.now()))
        #print(apple_eaten._live_receivers(Apple))

default_app_config = 'main.AppConfig'
