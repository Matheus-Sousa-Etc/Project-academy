from django.urls import path
from . import views

app_name ="lanch"

urlpatterns = [
    path("home/", views.home_html, name="home"),
]