from django.shortcuts import render, redirect
from .models import *
from estoque.models import EntradaItem, SaidaItem
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    #funcionarios = Funcionario.objects.all().filter(ativo=True)
    obras = Obra.objects.all()

    context = {}
    context['obras'] = obras
    #context['funcionarios'] = funcionarios

    return render(request, 'indexObra.html', context)

def obra_detalhe(request, pk):
    obras = Obra.objects.all().filter(id=pk)
    entradas = EntradaItem.objects.all().filter(obra_id=pk)
    saidas = SaidaItem.objects.all().filter(obra_id=pk)

    context = {}
    context['obras'] = obras
    context['entradas'] = entradas
    context['saidas'] = saidas

    return render(request, 'obra_detalhe.html', context)

def obra_add(request):
    form = ObraForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_obra");</script>' % (instance.pk, instance))
    return render(request, 'add_obra.html', {"form" : form})

def add_obra(request):
    form = ObraForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_obra");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_obra.html', {"form" : form})

def add_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_cliente");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_cliente.html', {"form" : form})

def obra_excluir(request, pk, args):
    obras = Obra.objects.filter(id=pk)
    
    context = {}
    context['obras'] = obras

    """ if(request.GET.get('excluir')): """
    if(args == 1):
        Obra.objects.filter(id=pk).delete()
        return redirect('obra:index')
    return redirect('obra:index')

def index_obra(request, pk):
    obras = Obra.objects.get(id=pk)

    saidas = SaidaItem.objects.all().filter(emprestimo=False).filter(obra=pk).order_by('data')
    entradas = EntradaItem.objects.all().filter(emprestimo=False).filter(obra=pk).order_by('data')

    context = {}
    context['obras'] = obras
    context['saidas'] = saidas
    context['entradas'] = entradas

    total_entradas = 0
    total_saidas = 0

    for entrada in entradas:
        total_entradas += (entrada.item.valor * entrada.quantidade)
    
    for saida in saidas:
        total_saidas += (saida.item.valor * saida.quantidade)

    saldo = total_saidas - total_entradas

    context['total_entradas'] = total_entradas
    context['total_saidas'] = total_saidas
    context['saldo'] = saldo

    return render(request, 'relatorios/relatorio_obra.html', context)
    