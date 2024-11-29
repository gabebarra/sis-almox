from django.shortcuts import render, redirect
from .models import *
from .forms import *
from obra.models import Obra
from funcionario.models import Funcionario
from django.http import HttpResponse, HttpResponseRedirect
from core.utils import formatar_data

def index_estoque(request):
    categorias = Categoria.objects.all()
    itens = Item.objects.all()
    prateleiras = Prateleira.objects.all()

    context = {}
    context['categorias'] = categorias
    context['prateleiras'] = prateleiras

    if request.method == 'GET':
        categoria = request.GET.get('id_categoria')
        prateleira = request.GET.get('id_prateleira')

    if (request.GET.get('gerar')):
        if (int(categoria) == 0):
            context['categoria'] = str("Todas Categorias")
            
        elif (int(categoria) > 0):
            cat = Categoria.objects.all().filter(id=categoria)
            itens = itens.filter(categoria=categoria)
            for categoria in cat:
                context['categoria'] = categoria

        if (int(prateleira) == 0):
            context['prateleira'] = str("Todas Prateleiras")
            prateleira = ""
        elif (int(prateleira) > 0):
            prat = Prateleira.objects.all().filter(id=prateleira)
            itens = itens.filter(prateleira=prateleira)
            for prateleira in prat:
                context['prateleira'] = prateleira

        itens = itens.order_by('nome')
        context['itens'] = itens

        return render(request, 'relatorios/relatorio_estoque.html', context)

    return render(request, 'relatorios/index_estoque.html', context)

def index_saida(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    prateleiras = Prateleira.objects.all()
    funcionarios = Funcionario.objects.all()
    obras = Obra.objects.all()

    saidas = SaidaItem.objects.all().filter(emprestimo=False)

    context = {}
    context['itens'] = itens
    context['categorias'] = categorias
    context['prateleiras'] = prateleiras
    context['funcionarios'] = funcionarios
    context['obras'] = obras

    if request.method == 'GET':
        item = request.GET.get('id_item')
        categoria = request.GET.get('id_categoria')
        prateleira = request.GET.get('id_prateleira')
        funcionario = request.GET.get('id_funcionario')
        obra = request.GET.get('id_obra')

    if (request.GET.get('gerar')):
        if (int(item) == 0):
            context['item'] = str("Todos")
        elif (int(item) > 0):
            nome_item = Item.objects.get(id=item)
            saidas = saidas.filter(item=item)
            context['item'] = nome_item

        if (int(categoria) == 0):
            context['categoria'] = str("Todas")
        elif (int(categoria) > 0):
            nome_categoria = Categoria.objects.get(id=categoria)
            saidas = saidas.filter(item__categoria=categoria)
            context['categoria'] = nome_categoria

        if (int(prateleira) == 0):
            context['prateleira'] = str("Todas")
        elif (int(prateleira) > 0):
            nome_prateleira = Prateleira.objects.get(id=prateleira)
            saidas = saidas.filter(item__prateleira=prateleira)
            context['prateleira'] = nome_prateleira
        
        if (int(funcionario) == 0):
            context['funcionario'] = str("Todos")
        elif (int(funcionario) > 0):
            nome_funcionario = Funcionario.objects.get(id=funcionario)
            saidas = saidas.filter(funcionario=funcionario)
            context['funcionario'] = nome_funcionario

        if (int(obra) == 0):
            context['obra'] = str("Todas")
        elif (int(obra) > 0):
            nome_obra = Obra.objects.get(id=obra)
            saidas = saidas.filter(obra=obra)
            context['obra'] = nome_obra

        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final

        saidas = saidas.filter(data__range=(data_inicial, data_final)).order_by('data')
        context['saidas'] = saidas
        

        return render(request, 'relatorios/relatorio_saida.html', context)

    return render(request, 'relatorios/index_saida.html', context)

def index_emprestimo(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    prateleiras = Prateleira.objects.all()
    funcionarios = Funcionario.objects.all()
    obras = Obra.objects.all()

    saidas = SaidaItem.objects.all().filter(emprestimo=True)

    context = {}
    context['itens'] = itens
    context['categorias'] = categorias
    context['prateleiras'] = prateleiras
    context['funcionarios'] = funcionarios
    context['obras'] = obras

    if request.method == 'GET':
        item = request.GET.get('id_item')
        categoria = request.GET.get('id_categoria')
        prateleira = request.GET.get('id_prateleira')
        funcionario = request.GET.get('id_funcionario')
        obra = request.GET.get('id_obra')

    if (request.GET.get('gerar')):
        if (int(item) == 0):
            context['item'] = str("Todos")
        elif (int(item) > 0):
            nome_item = Item.objects.get(id=item)
            saidas = saidas.filter(item=item)
            context['item'] = nome_item

        if (int(categoria) == 0):
            context['categoria'] = str("Todas")
        elif (int(categoria) > 0):
            nome_categoria = Categoria.objects.get(id=categoria)
            saidas = saidas.filter(item__categoria=categoria)
            context['categoria'] = nome_categoria

        if (int(prateleira) == 0):
            context['prateleira'] = str("Todas")
        elif (int(prateleira) > 0):
            nome_prateleira = Prateleira.objects.get(id=prateleira)
            saidas = saidas.filter(item__prateleira=prateleira)
            context['prateleira'] = nome_prateleira
        
        if (int(funcionario) == 0):
            context['funcionario'] = str("Todos")
        elif (int(funcionario) > 0):
            nome_funcionario = Funcionario.objects.get(id=funcionario)
            saidas = saidas.filter(funcionario=funcionario)
            context['funcionario'] = nome_funcionario

        if (int(obra) == 0):
            context['obra'] = str("Todas")
        elif (int(obra) > 0):
            nome_obra = Obra.objects.get(id=obra)
            saidas = saidas.filter(obra=obra)
            context['obra'] = nome_obra

        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final

        saidas = saidas.filter(data__range=(data_inicial, data_final)).order_by('data')
        context['saidas'] = saidas
        

        return render(request, 'relatorios/relatorio_emprestimo.html', context)

    return render(request, 'relatorios/index_emprestimo.html', context)

def index_entrada(request):
    itens = Item.objects.all()
    categorias = Categoria.objects.all()
    prateleiras = Prateleira.objects.all()
    funcionarios = Funcionario.objects.all()
    obras = Obra.objects.all()

    entradas = EntradaItem.objects.all()

    context = {}
    context['itens'] = itens
    context['categorias'] = categorias
    context['prateleiras'] = prateleiras
    context['funcionarios'] = funcionarios
    context['obras'] = obras

    if request.method == 'GET':
        item = request.GET.get('id_item')
        categoria = request.GET.get('id_categoria')
        prateleira = request.GET.get('id_prateleira')
        funcionario = request.GET.get('id_funcionario')
        obra = request.GET.get('id_obra')

    if (request.GET.get('gerar')):
        if (int(item) == 0):
            context['item'] = str("Todos")
        elif (int(item) > 0):
            nome_item = Item.objects.get(id=item)
            entradas = entradas.filter(item=item)
            context['item'] = nome_item

        if (int(categoria) == 0):
            context['categoria'] = str("Todas")
        elif (int(categoria) > 0):
            nome_categoria = Categoria.objects.get(id=categoria)
            entradas = entradas.filter(item__categoria=categoria)
            context['categoria'] = nome_categoria

        if (int(prateleira) == 0):
            context['prateleira'] = str("Todas")
        elif (int(prateleira) > 0):
            nome_prateleira = Prateleira.objects.get(id=prateleira)
            entradas = entradas.filter(item__prateleira=prateleira)
            context['prateleira'] = nome_prateleira
        
        if (int(funcionario) == 0):
            context['funcionario'] = str("Todos")
        elif (int(funcionario) > 0):
            nome_funcionario = Funcionario.objects.get(id=funcionario)
            entradas = entradas.filter(funcionario=funcionario)
            context['funcionario'] = nome_funcionario

        if (int(obra) == 0):
            context['obra'] = str("Todas")
        elif (int(obra) > 0):
            nome_obra = Obra.objects.get(id=obra)
            entradas = entradas.filter(obra=obra)
            context['obra'] = nome_obra

        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final

        entradas = entradas.filter(data__range=(data_inicial, data_final)).order_by('data')
        context['entradas'] = entradas
        

        return render(request, 'relatorios/relatorio_entrada.html', context)

    return render(request, 'relatorios/index_entrada.html', context)
    