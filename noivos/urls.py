from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Exibe a página inicial em /noivos/
    path('lista_convidados/', views.lista_convidados, name="lista_convidados"),  # Página de lista de convidados
]
