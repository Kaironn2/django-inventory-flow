from django import forms

from . import models

INPUT_CLASSES = (
    'w-full bg-midnight text-slate-100 '
    'border border-slate-700 rounded p-2'
)


class InflowForm(forms.ModelForm):
    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
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
