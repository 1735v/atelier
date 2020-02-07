from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'main_app/base.html')

def home_page(request):
    return render(request, 'main_app/home.html')