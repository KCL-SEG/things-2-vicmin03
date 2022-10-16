"""Forms of the project."""

from django import forms

class ThingsForm(forms.Form):
    name = forms.CharField(label="Name:", max_length=30)
    description = forms.CharField(label="Description:", max_length=400, widget=forms.Textarea)
    quantity = forms.IntegerField(label="Quantity:", widget=forms.NumberInput())
