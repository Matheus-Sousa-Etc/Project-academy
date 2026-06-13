from django.shortcuts import render, redirect, get_object_or_404 # O get_object_or_404 pega um objeto do banco de dados ou da error 404 caso não ache 
from django.http import HttpResponse
from .models import Aulas, lanchonete #Importando a tabela Aulas do banco de dados
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

def login_admin_html(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    else:
        #pega as informações do banco de dados para a autenticação
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)#autenticação do usuario usando tag propria do django

        if user and user.is_superuser:
            login(request, user)
            return redirect ('lanch:home-admin') #caso o usuario logue e seja autenticado, vai para a pagina home
        else:
            return HttpResponse("erro de login, apenas adm possuem acesso") #erro no login

def home_html(request):
    musculacao = Aulas.objects.get(modalidade='musculação') #Pega o objeto musculação do banco, armazena em musculacao.
    crossfit = Aulas.objects.get(modalidade='crossfit')
    pilates = Aulas.objects.get(modalidade='pilates')
    jump = Aulas.objects.get(modalidade='jump')
    contexto ={
        'musculacao': musculacao,
        'crossfit': crossfit,
        'pilates': pilates,
        'jump': jump,
    }

    return render(request, 'home/home.html' ,contexto)

def home_admin_html(request):
    #verfica se o usuario é um superuser, ou seja, um admin
    if not request.user.is_superuser:
        return redirect("home")
    return render(request, 'home/home-admin.html')

# Views do Menu
def admin_html(request):
    return render(request, 'home/admin.html')

def carrinho_html(request):
    return render(request, 'loja/carrinho.html')

#Views da Loja
def suplementos_html(request):
    whey = lanchonete.objects.get(salgado = 'whey')
    #creatina = lanchonete.objects.get(salgado = '')
    #hipercalorico = lanchonete.objects.get(salgado = '')
    #preTreino = lanchonete.objects.get(salgado = '')
    context = {
        'whey': whey
    }
    return render(request, 'loja/suplementos.html', context)

def equipamentos_html(request):
    return render(request, 'loja/equipamentos.html')

#Pop ups
def vagas(request, id):
    modalidade = get_object_or_404(Aulas, id=id) # Se o id passado nos parametros for igual ao id que está no banco ele funciona, senao da erro 404
    if modalidade.vagas > 0: # Se nao tiver vagas vai pra fila
        modalidade.vagas -= 1
        modalidade.save() # Salva a alteração
    #else:
        #fila += 1
    return redirect ('lanch:home')

#Funcionalidades da loja
def loja(request, id): # Meu Deus 
    suplemento = get_object_or_404(lanchonete,id=id)
    if suplemento.estoque > 0:
        suplemento.estoque -=1
        suplemento.faturamento += suplemento.preço
        suplemento.save()
    return redirect ('lanch:suplementos')