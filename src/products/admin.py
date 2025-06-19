from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(models.Product, ProductAdmin)
