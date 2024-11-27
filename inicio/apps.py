from django.apps import AppConfig

class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inicio'

class NomedoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastrar'

    def ready(self):
        import cadastrar.signals