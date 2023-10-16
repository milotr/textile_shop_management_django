from .models import *
from django import forms

class LengthCalculatorForm(forms.Form):
    cân_nặng_mẫu_vải = forms.FloatField()
    cân_nặng_cả_cây = forms.FloatField()
    chiều_cao = forms.FloatField()