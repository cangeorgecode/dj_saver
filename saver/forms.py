from .models import Saving
from django.forms import ModelForm
from django import forms

class SavingForm(ModelForm):
    field_order = ['item_name', 'item_cost']

    class Meta:
        model = Saving
        fields = {'item_name', 'item_cost',}

    def __init__(self, *args, **kwargs):
        super(SavingForm, self).__init__(*args, **kwargs)

        self.fields['item_name'].label = ''
        self.fields['item_name'].widget.attrs['class'] = 'form-control'
        self.fields['item_name'].widget.attrs['placeholder'] = 'Item'

        self.fields['item_cost'].label = ''
        self.fields['item_cost'].widget.attrs['class'] = 'form-control'
        self.fields['item_cost'].widget.attrs['placeholder'] = 'Cost'