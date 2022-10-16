"""Forms of the project."""

from django import forms
from .models import Thing

class ThingsForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea, 'quantity':forms.NumberInput()}


    # name = forms.CharField(label="Name:", max_length=30)
    # description = forms.CharField(label="Description:", max_length=400, widget=forms.Textarea)
    # quantity = forms.IntegerField(label="Quantity:", widget=forms.NumberInput())
