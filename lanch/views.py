from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User # é mais facil usar a model propria do django por conta verificação :)
from django.contrib.auth import authenticate, login #essa bosta serve pra autenticação do usuário
# Create your views here.
def login_html(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    else:
        #pega as informações do banco de dados para a autenticação
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)#autenticação do usuario usando tag propria do django

        if user:
            login(request, user)
            return redirect ('lanch:home') #caso o usuario logue e seja autenticado, vai para a pagina home
        else:
            return HttpResponse("erro de login") #erro no login

def cadastro_html(request):
    if request.method== "GET":
        return render(request, 'login/cadastro.html')
    else: 
        #envia os dados para o banco de dados
        username = request.POST.get('email')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        numero = request.POST.get('numero')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')

        user = User.objects.filter(username=username).first() # verficação da existencia do usuario no banco de dados

        if user:
        
            return HttpResponse ("usuario já existente")
        
        usuario = User.objects.create_user(username=email,password=senha) #cria o usuario/salva as infos no bd
        

        return redirect ('lanch:home')

def home_html(request):
    return render(request, 'home/home.html')

# Views do Menu
def admin_html(request):
    return render(request, 'home/admin.html')

# Views das aulas
def musculo_html(request):
    return render(request, 'aulas/musculo.html')

def crossfit_html(request):
    return render(request, 'aulas/crossfit.html')

#Views da lanchonete
def lanches_html(request):
    return render(request, 'lanchonete/lanches.html')

def bebidas_html(request):
    return render(request, 'lanchonete/bebidas.html')

