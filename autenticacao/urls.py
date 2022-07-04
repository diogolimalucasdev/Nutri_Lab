from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"), #agora preciso ir em views e criar uma função
    path('logar/', views.logar, name="logar"),
    path('sair/', views.sair, name="sair"),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta")

   
]