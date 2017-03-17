from django import forms

from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ['user']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            }),
            'details': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            }),
            'other_features': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            }),
            'delivery_date': forms.DateInput(attrs={
                'class': 'datepicker'
            })
        }
