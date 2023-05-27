from django.apps import AppConfig


class SupervisorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'supervisor'
    def ready(self):
        import supervisor.signals  # Import the signals module