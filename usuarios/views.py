from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()
    
    if request.POST.get('next', None) not in ('cadastro', 'login', 'logout', '', '/') and not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha_login'].value()
            
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{usuario.get_username()} logado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login!')
                return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha,
            )
            
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    user = auth.get_user(request)
    user = '' if str(user) == 'AnonymousUser' else user
    messages.success(request, f'{user} Deslogado com sucesso!')
    auth.logout(request)
    return redirect('login')