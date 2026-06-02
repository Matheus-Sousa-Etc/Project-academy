from django.db import models
    

# Create your models here
from django.db import models

class User(models.Model):
  nome = models.CharField(max_length=30)
  email = models.CharField(max_length=100)
  senha = models.CharField(max_length=50)
  aula = models.IntegerField(max_length=50)

  class admin(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    cref = models.CharField(max_length=6)

class Aulas(models.Model):
 modalidade = models.CharField(max_length=30)
 vagas = models.IntegerField(max_length=2)


class lanchonete(models.Model):
  salgado = models.CharField(max_length=15)
  preço = models.CharField(max_length=10)
  estoque = models.CharField(max_length=100)
  faturamento = models.IntegerField(max_length=256)
 
