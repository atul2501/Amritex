from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1> This is a pharma company </h1>")

def contact(request):
    return HttpResponse("<h1> this is Amritex Contact page :Contact page </h1>")