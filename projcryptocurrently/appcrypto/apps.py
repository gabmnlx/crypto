from django.apps import AppConfig


class AppcryptoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appcrypto'

    def ready(self):
        from jobs import updater
        print('Running background job processes...')
        updater.start()