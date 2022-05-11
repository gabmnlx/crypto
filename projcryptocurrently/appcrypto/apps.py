from django.apps import AppConfig


class AppcryptoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appcrypto'

    def ready(self):
        from jobs import updater
        updater.start()