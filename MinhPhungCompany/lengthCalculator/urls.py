from django.urls import path
from . import views
from lengthCalculator.views import length_calculator

urlpatterns = [
    path("lengthCalculator", length_calculator.as_view(), name="lengthCalculator"),
]
