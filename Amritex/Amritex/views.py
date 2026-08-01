from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def carrers(request):
    return render(request, 'carrers.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def updates(request):
    return render(request, 'updates.html')

def product(request):
    return render(request,'product.html')