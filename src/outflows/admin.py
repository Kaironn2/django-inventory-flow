from django.contrib import admin

from . import models


class OutflowAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Outflow, OutflowAdmin)
