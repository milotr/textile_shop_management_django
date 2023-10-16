from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("charts", views.charts, name="charts"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    # path("register", views.register, name="register"),
    path("customerTable", views.customerTable, name="customerTable"),
    path("typeTable", views.typeTable, name="typeTable"),
    path("colorTable/<str:pk>", views.colorTable, name="colorTable"),
    path("rollTable/<str:pk>", views.rollTable, name="rollTable"),
    path("orderTable", views.orderTable, name="orderTable"),
    path("customer/<str:pk>", views.customer, name="customer"),
    path("formCustomer", views.formCustomer, name="formCustomer"),
    path("formOrder", views.formOrder, name="formOrder"),
    path("formRoll", views.formRoll, name="formRoll"),
    path("formType", views.formType, name="formType"),
    path("formColor/", views.formColor, name="formColor"),
    path("updateCustomer/<str:pk>", views.updateCustomer, name="updateCustomer"),
    path("updateType/<str:pk>", views.updateType, name="updateType"),
    path("updateColor/<str:pk>", views.updateColor, name="updateColor"),
    path("updateRoll/<str:pk>", views.updateRoll, name="updateRoll"),
    path("updateOrder/<str:pk>", views.updateOrder, name="updateOrder"),
    path("deleteCustomer/<str:pk>", views.deleteCustomer, name="deleteCustomer"),
    path("deleteType/<str:pk>", views.deleteType, name="deleteType"),
    path("deleteColor/<str:pk>", views.deleteColor, name="deleteColor"),
    path("deleteRoll/<str:pk>", views.deleteRoll, name="deleteRoll"),
    path("deleteOrder/<str:pk>", views.deleteOrder, name="deleteOrder"),
    path(
        "deleteOrderCustomer/<str:pk>",
        views.deleteOrderCustomer,
        name="deleteOrderCustomer",
    ),
    path(
        "formOrderCustomer/<str:pk>", views.formOrderCustomer, name="formOrderCustomer"
    ),
]
