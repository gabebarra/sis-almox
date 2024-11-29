from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from funcionario.models import Funcionario
from obra.models import Obra
from veiculo.models import Veiculo
from estoque.models import Item
# Create your views here.

def login_sistema(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('core:index')
        else:
            form_login = AuthenticationForm()

    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login} )

def logout_sistema(request):

    logout(request)
    return redirect('core:index')

def index(request):
    context = {}
    context['usuario'] = request.user

    funcionarios = Funcionario.objects.filter(ativo=True).count()
    obras = Obra.objects.count()
    veiculos = Veiculo.objects.count()
    itens = Item.objects.count()

    context['funcionarios'] = funcionarios
    context['obras'] = obras
    context['veiculos'] = veiculos
    context['itens'] = itens

    return render(request, 'index_inicio.html', context)