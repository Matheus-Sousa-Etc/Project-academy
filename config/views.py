from django.shortcuts import render




def login_html(request):
    return render(request, 'login/login.html')

# def home_html(request):
#     return render(request, 'home/home.html')