from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('historia/', views.historia, name = 'historia'),
    path('musicos/', views.musicos, name = 'musicos'),
    path('', views.index, name = 'diretoria'),
    path('', views.index, name = 'galeria'),
    path('', views.index, name = 'agenda'),
    path('', views.index, name = 'contato'),
]