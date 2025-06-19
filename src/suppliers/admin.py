from django.contrib import admin

from . import models


class SupplierAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Supplier, SupplierAdmin)
