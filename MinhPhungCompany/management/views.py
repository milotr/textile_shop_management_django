from calendar import c
from multiprocessing import context
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

def customerTable(request):
    customers = Customer.objects.all()
    # the string in the dictionary will be used in template
    context = {
        'customers' : customers,
    } 
    return render(request, 'management/customerTable.html', context)

def productTable(request):
    products = Product.objects.all()
    # the string in the dictionary will be used in template
    context = {
        'products' : products,
    } 
    return render(request, 'management/productTable.html', context)

def login(request):
    context = {}
    return render(request, 'management/login.html', context)

def order(request):
    # customers = Customer.objects.get(id=pk)
    # orders = customer.order_set.all()
    # context = {
    #     'customers' : customers,
    #     'orders' : orders,
    # }
    orders = Order.objects.all()
    products = product.order_set.all()
    context = {
        'orders' : orders,
        'products' : products,
    }
    return render(request, 'management/order.html', context)