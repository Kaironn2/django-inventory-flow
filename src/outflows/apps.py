from django.apps import AppConfig


class OutflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outflows'

    def ready(self):  # noqa: PLR6301
        import outflows.signals  # noqa: F401, PLC0415
