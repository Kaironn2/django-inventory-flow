from django.db import models


class Brand(models.Model):
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
    def __str__(self):
        return self.name
