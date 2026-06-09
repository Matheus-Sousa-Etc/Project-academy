from django.urls import path
from . import views

app_name ="lanch"

urlpatterns = [
    path("login/", views.login_html, name="login"),
    path("login-admin/", views.login_admin_html, name="login-admin"),
    path("cadastro/", views.cadastro_html, name="cadastro"),
    path("home/", views.home_html, name="home"),
    path("home-admin/", views.home_admin_html, name="home-admin"),
    path("admin/", views.admin_html, name="admin"),
    path("suplementos/", views.suplementos_html, name="suplementos"),
    path("equipamentos/", views.equipamentos_html, name="equipamentos"),
    path("carrinho/", views.carrinho_html, name="carrinho"),
]