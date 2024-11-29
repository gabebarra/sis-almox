from django.shortcuts import render, redirect
from .models import *
from estoque.models import EntradaItem, SaidaItem
from .forms import *
import datetime
from datetime import date
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    funcionarios = Funcionario.objects.all().filter(ativo=True)

    context = {}
    context['funcionarios'] = funcionarios

    return render(request, 'index.html', context)

def funcionario_add(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_funcionario");</script>' % (instance.pk, instance))  
    return render(request, 'funcionario_add.html', {"form" : form})

def funcionario_add_norefresh(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_funcionario");</script>' % (instance.pk, instance))
    return render(request, 'funcionario_add.html', {"form" : form})

def formset_funcionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        adicionar = request.POST.get('add')
        if(request.POST.get('add')):
            adicionar = False
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_funcionario");</script>' % (instance.pk, instance))
    return render(request, 'formset_funcionario.html', {"form" : form})

def add_funcionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_funcionario");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_funcionario.html', {"form" : form})

def edit_funcionario(request, pk):
    funcionario = Funcionario.objects.all().filter(id=pk)
    padrao = {}

    for func in funcionario:
        padrao['nome'] = func.nome
        padrao['funcao'] = func.funcao
        padrao['empresa'] = func.empresa
        padrao['data'] = func.get_data

    form = Edit_FuncionarioForm(request.POST or None, initial=padrao)

    if form.is_valid():
        funcionario.update(nome=form.cleaned_data['nome'],
                            funcao=form.cleaned_data['funcao'],
                            empresa=form.cleaned_data['empresa'],
                            data=form.cleaned_data['data'],)
        instance = form.save(commit=False)
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_funcionario");</script>' % (instance.pk, instance))
    return render(request, 'funcionario_edit.html', {"form" : form})

def funcao_add(request):
    form = FuncaoForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_funcao");</script>' % (instance.pk, instance))
    return render(request, 'funcao_add.html', {"form" : form})

def empresa_add(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_empresa");</script>' % (instance.pk, instance))
    return render(request, 'empresa_add.html', {"form" : form})

def funcionario_detalhe(request, pk):
    funcionarios = Funcionario.objects.all().filter(id=pk)
    saidas = SaidaItem.objects.all().filter(funcionario_id=pk)
    entradas = EntradaItem.objects.all().filter(funcionario_id=pk)
    epis = saidas.filter(emprestimo=True).filter(item__categoria__categoria='EPI').filter(entregue=False)
    context = {}
    
    hoje = date.today()
    for saida in epis:
        venc = saida.data + datetime.timedelta(days=saida.item.vencimento)
        saida.trocar = False
        if (venc < hoje):
            saida.trocar = True
        saida.vencimento = venc
        

    context['saida_epi'] = epis
    context['funcionarios'] = funcionarios
    context['saidas'] = saidas
    context['entradas'] = entradas

    return render(request, 'funcionario_detalhe.html', context)

def funcionario_excluir(request, pk, args):

    if(args == 1):
        Funcionario.objects.filter(id=pk).delete()
        return redirect('funcionario:index')
    return redirect('funcionario:index')

def index_funcionario(request, pk):
    context = {}
    funcionario = Funcionario.objects.get(id=pk)
    entradas = EntradaItem.objects.filter(funcionario=pk)

    emprestimos = SaidaItem.objects.filter(funcionario=pk).filter(emprestimo=True).filter(entregue=False)
    epis = emprestimos.filter(item__categoria__categoria='EPI')
    pendentes = emprestimos.exclude(item__categoria__categoria='EPI')

    context['entradas'] = entradas
    context['emprestimos'] = emprestimos
    context['epis'] = epis
    context['pendentes'] = pendentes
    context['funcionario'] = funcionario

    hoje = date.today()
    for saida in epis:
        venc = saida.data + datetime.timedelta(days=saida.item.vencimento)
        saida.trocar = False
        if (venc < hoje):
            saida.trocar = True
        saida.vencimento = venc

    return render(request, 'relatorios/relatorio_funcionario.html', context)