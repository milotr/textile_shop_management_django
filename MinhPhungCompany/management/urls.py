from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("charts", views.charts, name="charts"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    # path("register", views.register, name="register"),
    path("customerTable", views.customerTable, name="customerTable"),
    path("productTable", views.productTable, name="productTable"),
    path("typeTable/<str:pk>", views.typeTable, name="typeTable"),
    path("colorTable", views.colorTable, name="colorTable"),
    path("orderTable", views.orderTable, name="orderTable"),
    path("customer/<str:pk>", views.customer, name="customer"),
    path("formCustomer", views.formCustomer, name="formCustomer"),
    path("formOrder", views.formOrder, name="formOrder"),
    path("formProduct", views.formProduct, name="formProduct"),
    path("formType", views.formType, name="formType"),
    path("formColor", views.formColor, name="formColor"),
    path("updateCustomer/<str:pk>", views.updateCustomer, name="updateCustomer"),
    path("updateProduct/<str:pk>", views.updateProduct, name="updateProduct"),
    path("updateOrder/<str:pk>", views.updateOrder, name="updateOrder"),
    path("deleteCustomer/<str:pk>", views.deleteCustomer, name="deleteCustomer"),
    path("deleteProduct/<str:pk>", views.deleteProduct, name="deleteProduct"),
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
