from django.shortcuts import render
from usuarios.models import *

def login(request):
    return render(request, 'usuarios/login.html')


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')