from django import forms

from . import models

INPUT_CLASSES = (
    'w-full bg-midnight text-slate-100 '
    'border border-slate-700 rounded p-2'
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            'title', 'category', 'brand', 'description',
            'serie_number', 'cost_price', 'selling_price'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'brand': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4
            }),
            'serie_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'cost_price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
