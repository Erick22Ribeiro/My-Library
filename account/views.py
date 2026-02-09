from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

# Create your views here.
def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username = email, password = senha)

        if user is not None:
            print('login')
            auth_login(request, user)
            return redirect('/home/')
        
        else:
            erro = "Email ou senha inválidos"
            return render(request, 'account/login.html', {'erro':erro})

    return render(request, 'account/login.html')


def cadastro(request):

    if request.method == 'POST':

        primeiro_nome = request.POST.get('primeiro_nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.create_user(
            first_name = primeiro_nome,
            last_name = sobrenome,
            email = email,
            username = email,
            password = senha,
        )

        auth_login(request, user)

        return redirect('/home/')

    return render(request, 'account/cadastro.html')