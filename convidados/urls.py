from django.urls import path
from . import views

urlpatterns = [
    path('', views.convidados, name='convidados'),
    path('responder_presenca/', views.responder_presenca, name='responder_presenca'),
    path('reservar_presente/<int:id>/', views.reservar_presente, name='reservar_presente'),
    path('adicionar_acompanhante/', views.adicionar_acompanhante, name='adicionar_acompanhante'),  # Adiciona esta linha
]
