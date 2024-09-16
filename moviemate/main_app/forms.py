from django import forms
from .models import Watches

class WatchesForm(forms.ModelForm):
  class Meta:
    model = Watches
    fields = ['date', 'time']
    widgets = {
      'date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      ),
    }