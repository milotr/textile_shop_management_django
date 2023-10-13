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
from django.forms import inlineformset_factory

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

# -------------------------------------------------------------------------------------------
# LOGIN AND LOGOUT
# -------------------------------------------------------------------------------------------

#Login views: allowed unauthenticated user to access
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

#Logout views: allowed logged in user to access
@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    return redirect("login")

# -------------------------------------------------------------------------------------------
# HOME VIEWS
# -------------------------------------------------------------------------------------------

#Home views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin", "employee"])
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    roll = Roll.objects.all()

    total_customer = customer.count()
    total_order = order.count()
    total_roll = roll.count()

    context = {
        "customer": customer,
        "order": order,
        "roll": roll,
        "total_customer": total_customer,
        "total_order": total_order,
        "total_roll": total_roll,
    }
    return render(request, "management/index.html", context)

# -------------------------------------------------------------------------------------------
# CHART VIEWS
# -------------------------------------------------------------------------------------------

#Chart views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def charts(request):
    context = {}
    return render(request, "management/charts.html", context)

# -------------------------------------------------------------------------------------------
# CUSTOMER PROFILE AND TABLE
# -------------------------------------------------------------------------------------------

#Customer table views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def customerTable(request):
    customer = Customer.objects.all()
    # the string in the dictionary will be used in template
    context = {
        "customer": customer,
    }
    return render(request, "management/tables/customerTable.html", context)

#Customer adding views: allowed logged in user and allowed user to access
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

# -------------------------------------------------------------------------------------------
# TYPE TABLE
# -------------------------------------------------------------------------------------------

#Type views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def typeTable(request):
    type = Type.objects.all()
    # the string in the dictionary will be used in template
    context = {
        "type": type,
    }
    return render(request, "management/tables/typeTable.html", context)

# -------------------------------------------------------------------------------------------
# COLOR TABLE
# -------------------------------------------------------------------------------------------

#Color views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def colorTable(request, pk):
    type = Type.objects.get(type_id=pk)
    color = type.color_set.all()
    # the string in the dictionary will be used in template
    context = {
        "type": type,
        "color": color,
    }
    return render(request, "management/tables/colorTable.html", context)

# -------------------------------------------------------------------------------------------
# ROLL TABLE
# -------------------------------------------------------------------------------------------

#Roll views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def rollTable(request):
    roll = Roll.objects.all()
    # the string in the dictionary will be used in template
    context = {
        "roll": roll,
    }
    return render(request, "management/tables/rollTable.html", context)


# -------------------------------------------------------------------------------------------
# ORDER TABLE
# -------------------------------------------------------------------------------------------

#Order views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def orderTable(request):
    order = Order.objects.all()
    context = {
        "order": order,
    }
    return render(request, "management/tables/orderTable.html", context)

# -------------------------------------------------------------------------------------------
# FORM CUSTOMER
# -------------------------------------------------------------------------------------------

#Form adding Customer views: allowed logged in user and allowed user to access
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

#Form updating Customer views: allowed logged in user and allowed user to access
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

#Form deleting Customer views: allowed logged in user and allowed user to access
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

# -------------------------------------------------------------------------------------------
# FORM PRODUCT
# -------------------------------------------------------------------------------------------

#Form adding Product views: allowed logged in user and allowed user to access
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

#Form updating Product views: allowed logged in user and allowed user to access
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

#Form deleting Product views: allowed logged in user and allowed user to access
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
# -------------------------------------------------------------------------------------------
# FORM TYPE
# -------------------------------------------------------------------------------------------

#Form adding Type views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formType(request):
    form = TypeForm()

    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("typeTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formType.html", context)

#Form updating Type views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateType(request, pk):
    type = Type.objects.get(type_id=pk)
    form = TypeForm(instance=type)

    if request.method == "POST":
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save(),
            return redirect("typeTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formType.html", context)

#Form deleting Type views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteType(request, pk):
    type = Type.objects.get(type_id=pk)

    if request.method == "POST":
        type.delete()
        return redirect("typeTable")

    context = {
        "type": type,
    }
    return render(request, "management/forms/deleteType.html", context)
# -------------------------------------------------------------------------------------------
# COLOR TYPE
# -------------------------------------------------------------------------------------------

#Form adding Color views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formColor(request):
    form = ColorForm()

    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("colorTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formColor.html", context)

#Form updating Color views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateColor(request, pk):
    color = Color.objects.get(color_id=pk)
    form = ColorForm(instance=type)

    if request.method == "POST":
        form = ColorForm(request.POST, instance=type)
        if form.is_valid():
            form.save(),
            return redirect("colorTable")

    context = {
        "form": form,
    }
    return render(request, "management/forms/formColor.html", context)

#Form deleting Color views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteColor(request, pk):
    color = Color.objects.get(color_id=pk)

    if request.method == "POST":
        color.delete()
        return redirect("colorTable")

    context = {
        "color": color,
    }
    return render(request, "management/forms/deleteColor.html", context)

# -------------------------------------------------------------------------------------------
# FORM ORDER
# -------------------------------------------------------------------------------------------

#Form adding Order views: allowed logged in user and allowed user to access
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

#Form updating Order views: allowed logged in user and allowed user to access
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

#Form deleting Order views: allowed logged in user and allowed user to access
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

# -------------------------------------------------------------------------------------------
# FORM ORDER CUSTOMER
# -------------------------------------------------------------------------------------------

#Form Order Customer views: allowed logged in user and allowed user to access
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def formOrderCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product',), extra = 10)
    #form = OrderForm(initial={"customer": customer})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("customerTable")

    context = {
        "formset": formset,
    }
    return render(request, "management/forms/formOrderCustomer.html", context)

#Form deleting Order Customer views: allowed logged in user and allowed user to access
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