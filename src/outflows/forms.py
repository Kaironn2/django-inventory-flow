from django import forms
from django.core.exceptions import ValidationError

from . import models

INPUT_CLASSES = (
    'w-full bg-midnight text-slate-100 '
    'border border-slate-700 rounded p-2'
)


class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4
            }),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto'
                f'{product.title} é de {product.quantity}'
            )

        return quantity
