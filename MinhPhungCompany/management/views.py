from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers,
    }
    return render(request, 'management/index.html', context)

def charts(request):
    context = {}
    return render(request, 'management/charts.html', context)

def tables(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    # the string in the dictionary will be used in template
    context = {
        'customers' : customers,
        'products' : products,
    } 
    return render(request, 'management/tables.html', context)

def login(request):
    context = {}
    return render(request, 'management/login.html', context)