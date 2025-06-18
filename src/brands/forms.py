from django import forms

from . import models

INPUT_CLASSES = (
    'w-full bg-midnight text-slate-100 '
    'border border-slate-700 rounded p-2'
)


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'rows': 4
            }),
        }
