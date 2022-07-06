from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# serve para verificar se o usuario esta logado e deixar seguro a aplicação
@login_required(login_url = '/auth/logar/')
def pacientes(request):
    return render(request, 'pacientes.html')
