from django.shortcuts import render

# Create your views here.

def login_html(request):
    return render(request, 'login/login.html')

def home_html(request):
    return render(request, 'home/home.html')

def cadastro_html(request):
    return render(request, 'login/cadastro.html')