from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {}
    return render(request, 'management/index.html', context)

def charts(request):
    context = {}
    return render(request, 'management/charts.html', context)

def tables(request):
    context = {}
    return render(request, 'management/tables.html', context)

def login(request):
    context = {}
    return render(request, 'management/login.html', context)