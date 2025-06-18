from django import forms

from . import models


class BrandCreateForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'w-full bg-midnight text-slate-100 '
                    'border border-slate-700 rounded p-2'
                )
            }),
            'description': forms.Textarea(attrs={
                'class': (
                    'w-full bg-midnight text-slate-100 '
                    'border border-slate-700 rounded p-2'
                ),
                'rows': 4
            }),
        }
