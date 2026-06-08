from django.urls import path
from . import views

app_name ="lanch"

urlpatterns = [
    path("login/", views.login_html, name="login"),
    path("home/", views.home_html, name="home"),
    path("cadastro/", views.cadastro_html, name="cadastro"),
    path("admin/", views.admin_html, name="admin"),
    path("musculação/", views.musculo_html, name="musculo"),
    path("crossfit/", views.crossfit_html, name="crossfit"),
    path("lanches/", views.lanches_html, name="lanches"),
    path("bebidas/", views.bebidas_html, name="bebidas"),
]