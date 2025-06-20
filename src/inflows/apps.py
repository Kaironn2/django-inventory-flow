from django.apps import AppConfig


class InflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inflows'

    def ready(self):  # noqa: PLR6301
        import inflows.signals  # noqa: F401, PLC0415
