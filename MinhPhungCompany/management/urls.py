from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('charts', views.charts),
    path('customerTable',views.customerTable),
    path('productTable',views.productTable),
    path('', views.login)
]
