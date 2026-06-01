from django.shortcuts import render
from django.http import HttpResponse



def login_html(request):
    return render(request, 'login/login.html')