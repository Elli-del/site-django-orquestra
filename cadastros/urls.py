from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('historia/', views.historia, name = 'historia'),
    path('musicos/', views.musicos, name = 'musicos'),
    path('diretoria/', views.diretoria, name = 'diretoria'),
    path('', views.index, name = 'galeria'),
    path('', views.index, name = 'agenda'),
    path('', views.index, name = 'contato'),
    path('cadastrar_diretoria/', views.cadastrar_diretoria, name='cadastrar_diretoria'),
]