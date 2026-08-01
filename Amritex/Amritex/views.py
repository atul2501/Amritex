from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome to Amritex Project : Home Page</h1>")

def about(request):
    return HttpResponse("<h1> This is a pharma company </h1>")

def contact(request):
    return HttpResponse("<h1> this is Amritex Contact page :Contact page </h1>")