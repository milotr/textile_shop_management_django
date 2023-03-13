from calendar import c
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

# def register(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         form = CreateUserForm()
#         context = {"form": form}
#         if request.method == "POST":
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get("username")
#                 messages.success(request, "Account was created for " + user)
#                 return redirect("login")
#         return render(request, "management/register.html", context)


@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Tên người dùng hoặc mật khẩu sai.")
    context = {}
    return render(request, "management/login.html", context)


@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    return redirect("login")


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin", "employee"])
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    product = Product.objects.all()

    total_customer = customer.count()
    total_order = order.count()
    total_product = product.count()

    context = {
        "customer": customer,
        "order": order,
        "product": product,
        "total_customer": total_customer,
        "total_order": total_order,
        "total_product": total_product,
    }
    return render(request, "management/index.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def charts(request):
    context = {}
    return render(request, "management/charts.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def customerTable(request):
    customer = Customer.objects.all()
    # the string in the dictionary will be used in template
    context = {
        "customer": customer,
    }
    return render(request, "management/tables/customerTable.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def customer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    order = customer.order_set.all()
    context = {
        "customer": customer,
        "order": order,
    }
    return render(request, "management/tables/customer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def productTable(request):
    product = Product.objects.all()
    # the string in the dictionary will be used in template
    context = {
        "product": product,
    }
    return render(request, "management/tables/productTable.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def order(request):
    order = Order.objects.all()
    context = {
        "order": order,
    }
    return render(request, "management/tables/orderTable.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customerTable")
    context = {
        "form": form,
    }
    return render(request, "management/forms/formCustomer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customerTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formCustomer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customerTable")

    context = {
        "customer": customer,
    }
    return render(request, "management/forms/deleteCustomer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formOrderCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = OrderForm(initial={"customer": customer})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customerTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formOrder.html", context)


# def formOrderCustomer(request, pk):
#     order = Order.objects.get(order_id=pk)

#     if request.method == 'POST':
#         order.delete()
#         return redirect('orderTable')

#     context = {
#         'order' : order,
#     }
#     return render(request, 'management/forms/deleteOrder.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteOrderCustomer(request, pk):
    order = Order.objects.get(Order_id=pk)
    order = customer.order_set.all()

    if request.method == "POST":
        order.delete()
        return redirect("orderTable")

    context = {
        "customer": customer,
        "order": order,
    }

    return render(request, "management/forms/deleteOrderCustomer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orderTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formOrder.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateOrder(request, pk):
    order = Order.objects.get(order_id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orderTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formOrder.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteOrder(request, pk):
    order = Order.objects.get(order_id=pk)

    if request.method == "POST":
        order.delete()
        return redirect("orderTable")

    context = {
        "order": order,
    }
    return render(request, "management/forms/deleteOrder.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formProduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formProduct.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save(),
            return redirect("productTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formProduct.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteProduct(request, pk):
    product = Product.objects.get(product_id=pk)

    if request.method == "POST":
        product.delete()
        return redirect("productTable")

    context = {
        "product": product,
    }
    return render(request, "management/forms/deleteProduct.html", context)
