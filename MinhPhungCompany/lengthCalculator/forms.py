from .models import *
from django import forms

class LengthCalculatorForm(forms.Form):
    weight_10cm = forms.FloatField()
    weight = forms.FloatField()
    height = forms.FloatField()