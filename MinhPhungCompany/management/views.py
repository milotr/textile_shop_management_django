from calendar import c
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    total_products = products.count()

    context = {
        'customers' : customers,
        'orders' : orders,
        'products' : products,
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'total_products' : total_products,
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

def customer (request, pk):
    customer = Customer.objects.get(customer_id=pk)
    orders = customer.order_set.all()
    context = {
        'customers' : customer,
        'orders' : orders,
    }
    return render(request, 'management/customer.html', context)

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
    # products = product.order_set.all()
    context = {
        'orders' : orders,
        # 'products' : products, 
    }
    return render(request, 'management/order.html', context)

