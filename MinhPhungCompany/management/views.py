from calendar import c
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
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
    return render(request, 'management/tables/customerTable.html', context)

def customer (request, pk):
    customer = Customer.objects.get(customer_id=pk)
    orders = customer.order_set.all()
    context = {
        'customers' : customer,
        'orders' : orders,
    }
    return render(request, 'management/tables/customer.html', context)

def productTable(request):
    products = Product.objects.all()
    # the string in the dictionary will be used in template
    context = {
        'products' : products,
    } 
    return render(request, 'management/tables/productTable.html', context)

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
    # for hexcolor in orders:
    #     print('{}'.format(hexcolor.product.hexcolor))
    # products = product.order_set.all()
    context = {
        'orders' : orders,
        # 'hexcolor' : hexcolor,
        # 'products' : products, 
    }
    return render(request, 'management/tables/orderTable.html', context)

def formCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customerTable')
    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formCustomer.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('customerTable')

    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formCustomer.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customerTable')

    context = {
        'customer' : customer,
    }
    return render(request, 'management/forms/deleteCustomer.html', context)

def formOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderTable')

    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formOrder.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(order_id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orderTable')

    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formOrder.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(order_id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('orderTable')

    context = {
        'order' : order,
    }
    return render(request, 'management/forms/deleteOrder.html', context)

def formProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productTable')

    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formProduct.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save(),
            return redirect('productTable')

    context = {
        'form' : form,
    }
    return render(request, 'management/forms/formProduct.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(product_id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('productTable')

    context = {
        'product' : product,
    }
    return render(request, 'management/forms/deleteProduct.html', context)

