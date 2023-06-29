from django.apps import AppConfig


class AuthorProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "author_profile"


    def ready(self):
        import author_profile.signals
