from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro')
]