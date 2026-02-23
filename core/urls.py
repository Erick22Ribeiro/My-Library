from django.urls import path, include
from core import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('buscar/', views.buscar, name = 'buscar'),
    path('livros/', views.livros, name = 'livros')
]