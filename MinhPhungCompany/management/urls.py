from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('charts', views.charts, name = "charts"),
    path('customerTable',views.customerTable, name="customerTable"),
    path('productTable',views.productTable, name="productTable"),
    path('orderTable', views.order, name="orderTable"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('', views.login, name='login'),
]
