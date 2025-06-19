from django.contrib import admin

from . import models


class InflowAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Inflow, InflowAdmin)
