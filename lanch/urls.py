from django.urls import path
from . import views

app_name ="lanch"

urlpatterns = [
    path("login/", views.login_html, name="login"),
    path("home/", views.home_html, name="home"),
    path("cadastro/", views.cadastro_html, name="cadastro"),
    path("admin/", views.admin_html, name="admin"),
    path("suplementos/", views.suplementos_html, name="suplementos"),
    path("equipamentos/", views.equipamentos_html, name="equipamentos"),
]