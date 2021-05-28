from django.apps import AppConfig


# from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
# from .signals import create_profile, save_profile
class SignalsConfig(AppConfig):
    name = 'Signals'

    # import Signals.signals
    def ready(self):
        import Signals.signals
        import Caching.signals
        import Models.signals
        # post_save.connect(create_profile, sender='User')
        # post_save.connect(save_profile, sender='User')
