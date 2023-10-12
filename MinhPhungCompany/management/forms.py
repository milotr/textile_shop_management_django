from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = "__all__"

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
