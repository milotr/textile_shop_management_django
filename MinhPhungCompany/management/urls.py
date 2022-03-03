from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('charts', views.charts),
    path('tables',views.tables),
    path('', views.login)
]
