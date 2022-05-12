from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('charts', views.charts, name = "charts"),
    path('', views.login, name='login'),

    path('customerTable',views.customerTable, name="customerTable"),
    path('productTable',views.productTable, name="productTable"),
    path('orderTable', views.order, name="orderTable"),
    path('customer/<str:pk>', views.customer, name="customer"),

    path('formCustomer', views.formCustomer, name="formCustomer"),
    path('formOrder', views.formOrder, name="formOrder"),
    path('formProduct', views.formProduct, name="formProduct"),

    path('updateCustomer/<str:pk>', views.updateCustomer, name="updateCustomer"),
    path('updateOrder/<str:pk>', views.updateOrder, name="updateOrder"),
    path('updateProduct/<str:pk>', views.updateProduct, name="updateProduct"),

    path('deleteProduct/<str:pk>', views.deleteProduct, name="deleteProduct"),
    path('deleteCustomer/<str:pk>', views.deleteCustomer, name="deleteCustomer"),
    path('deleteOrder/<str:pk>', views.deleteOrder, name="deleteOrder"),
]
