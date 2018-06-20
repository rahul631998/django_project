from django import forms
from .models import data

class data(forms.ModelForm):
    class Meta:
        model = data
        fields = '__all__'
