from django.shortcuts import render, redirect
from .models import *
import json
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from core.utils import formatar_data
# Create your views here.

def index(request):
    veiculos = Veiculo.objects.all()
    context = {}
    context['veiculos'] = veiculos

    return render(request, 'veiculos/index.html', context)

def veiculo_detalhe(request, pk):
    consertos = Conserto.objects.all().filter(veiculo=pk)
    abastecimentos = Abastecimento.objects.all().filter(veiculo=pk)
    veiculo = Veiculo.objects.all().filter(id=pk)

    context = {}
    context['consertos'] = consertos
    context['abastecimentos'] = abastecimentos
    context['veiculo'] = veiculo

    return render(request, 'veiculos/veiculo_detalhe.html', context)

def veiculo_excluir(request, pk):
    veiculo = Veiculo.objects.all().filter(id=pk)
    context = {}
    context['veiculo'] = veiculo

    if(request.GET.get('excluir')):
        Veiculo.objects.filter(id=pk).delete()
        return HttpResponse('<script>opener.closePopup(window,  "#id_veiculo_excluir");</script>' )
    return render(request, 'veiculos/veiculo_excluir.html', context)

def veiculo_add(request):
    context = {}
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES)
    else:
        form = VeiculoForm()        
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_veiculo");</script>' % (instance.pk, instance))
    return render(request, 'veiculos/veiculo_add.html', context)

def conserto_add(request, pk):
    veiculo = Veiculo.objects.all().filter(id=pk)
    context = {}
    form = ConsertoForm(request.POST or None)
    context['form'] = form

    primary_key = 0
    for v in veiculo:
        primary_key = v.id

    context['primary_key'] = json.dumps(primary_key)

    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_conserto");</script>' % (instance.pk, instance))
    return render(request, 'consertos/conserto_add.html', context)

def conserto_excluir(request, pk):
    conserto = Conserto.objects.all().filter(id=pk)
    context = {}
    context['conserto'] = conserto

    if(request.GET.get('excluir')):
        Conserto.objects.filter(id=pk).delete()
        return HttpResponse('<script>opener.closePopup(window,  "#id_conserto_excluir");</script>' )
    return render(request, 'consertos/conserto_excluir.html', context)

def oficina_add(request):
    form = OficinaForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_oficina");</script>' % (instance.pk, instance))
    return render(request, 'consertos/oficina_add.html', context)

def categoria_add(request):
    form = CategoriaConsertoForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_categoria");</script>' % (instance.pk, instance))
    return render(request, 'consertos/categoria_add.html', context)

def abastecimento_add(request, pk):
    veiculo = Veiculo.objects.all().filter(id=pk)
    context = {}
    form = AbastecimentoForm(request.POST or None)
    context['form'] = form

    primary_key = 0
    for v in veiculo:
        primary_key = v.id

    context['primary_key'] = json.dumps(primary_key)

    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_abastecimento");</script>' % (instance.pk, instance))
    return render(request, 'abastecimento/abastecimento_add.html', context)

def abastecimento_excluir(request, pk):
    abastecimento = Abastecimento.objects.all().filter(id=pk)
    context = {}
    context['abastecimento'] = abastecimento

    if(request.GET.get('excluir')):
        Abastecimento.objects.filter(id=pk).delete()
        return HttpResponse('<script>opener.closePopup(window,  "#id_abastecimento_excluir");</script>' )
    return render(request, 'abastecimento/abastecimento_excluir.html', context)

def posto_add(request):
    form = PostoForm(request.POST or None)
    context = {}
    context['form'] = form

    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_posto");</script>' % (instance.pk, instance))
    return render(request, 'abastecimento/posto_add.html', context)

def excluir_veiculo(request, pk, args):

    if(args == 1):
        Veiculo.objects.filter(id=pk).delete()
        return redirect('veiculo:index')
    return redirect('veiculo:index')

def excluir_conserto(request, pk, args):
    resp_body = '<script>window.location=document.referrer</script>' # VOLTAR P/ URL ANTERIOR

    if(args == 1):
        Conserto.objects.filter(id=pk).delete()
        return HttpResponse(resp_body)
    return HttpResponse(resp_body)

def excluir_abastecimento(request, pk, args):
    resp_body = '<script>window.location=document.referrer</script>' # VOLTAR P/ URL ANTERIOR

    if(args == 1):
        Abastecimento.objects.filter(id=pk).delete()
        return HttpResponse(resp_body)
    return HttpResponse(resp_body)

def index_veiculo(request):
    veiculos = Veiculo.objects.all()
    oficinas = Oficina.objects.all()
    postos = Posto.objects.all()
    categorias = CategoriaConserto.objects.all()

    consertos = Conserto.objects.all()
    abastecimentos = Abastecimento.objects.all()
    
    context = {}
    context['veiculos'] = veiculos
    context['oficinas'] = oficinas
    context['postos'] = postos
    context['categorias'] = categorias

    if request.method == 'GET':
        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')
        veiculo = request.GET.get('id_veiculo')
        oficina = request.GET.get('id_oficina')
        posto = request.GET.get('id_posto')
        categoria = request.GET.get('id_categoria')

    if (request.GET.get('gerar')):
        context['veiculo'] = Veiculo.objects.get(id=veiculo)
        consertos = consertos.filter(veiculo=veiculo)
        abastecimentos = abastecimentos.filter(veiculo=veiculo)

        if (int(oficina) == 0):
            context['oficina'] = str("Todas")
        elif (int(oficina) > 0):
            context['oficina'] = Oficina.objects.get(id=oficina)
            consertos = consertos.filter(oficina=oficina)

        if (int(posto) == 0):
            context['posto'] = str("Todos")
        elif (int(posto) > 0):
            context['posto'] = Posto.objects.get(id=posto)
            abastecimentos = abastecimentos.filter(posto=posto)
        
        if (int(categoria) == 0):
            context['categoria'] = str("Todas")
        elif (int(categoria) > 0):
            context['categoria'] = CategoriaConserto.objects.get(id=categoria)
            consertos = consertos.filter(categoria=categoria)

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final

        consertos = consertos.filter(data__range=(data_inicial, data_final)).order_by('data')
        abastecimentos = abastecimentos.filter(data__range=(data_inicial, data_final)).order_by('data')
        context['consertos'] = consertos
        context['abastecimentos'] = abastecimentos

        conserto_total = 0
        abastecimento_total = 0

        for conserto in consertos:
            conserto_total += conserto.valor
        for abastecimento in abastecimentos:
            abastecimento_total += abastecimento.valor

        context['conserto_total'] = conserto_total
        context['abastecimento_total'] = abastecimento_total
        

        return render(request, 'relatorios/relatorio_veiculo.html', context)

    return render(request, 'relatorios/index_veiculo.html', context)

def index_abastecimento(request):
    abastecimentos = Abastecimento.objects.all()
    veiculos = Veiculo.objects.all()
    postos = Posto.objects.all()

    context = {}
    context['veiculos'] = veiculos
    context['postos'] = postos

    if request.method == 'GET':
        posto = request.GET.get('id_posto')
        veiculo = request.GET.get('id_veiculo')
    
    if (request.GET.get('gerar')):

        if (int(veiculo) == 0):
            context['veiculo'] = str("Todos")
        else:
            context['veiculo'] = Veiculo.objects.get(id=veiculo)
            abastecimentos = abastecimentos.filter(veiculo=veiculo)

        if (int(posto) == 0):
            context['posto'] = str("Todos")
        else:
            context['posto'] = Posto.objects.get(id=posto)
            abastecimentos = abastecimentos.filter(posto=posto)

        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final
        
        abastecimentos = abastecimentos.filter(data__range=(data_inicial, data_final)).order_by('data')
        context['abastecimentos'] = abastecimentos

        abastecimento_total = 0

        for abastecimento in abastecimentos:
            abastecimento_total += abastecimento.valor
        context['abastecimento_total'] = abastecimento_total

        return render(request, 'relatorios/relatorio_abastecimento.html', context)
    
    return render(request, 'relatorios/index_abastecimento.html', context)

def index_conserto(request):
    veiculos = Veiculo.objects.all()
    oficinas = Oficina.objects.all()
    categorias = CategoriaConserto.objects.all()
    consertos = Conserto.objects.all()

    context = {}
    context['veiculos'] = veiculos
    context['oficinas'] = oficinas
    context['categorias'] = categorias

    if (request.method == 'GET'):
        veiculo = request.GET.get('id_veiculo')
        oficina = request.GET.get('id_oficina')
        categoria = request.GET.get('id_categoria')

    if (request.GET.get('gerar')):

        if (int(veiculo) == 0):
            context['veiculo'] = "Todos"
        else:
            context['veiculo'] = Veiculo.objects.get(id=veiculo)
            consertos = consertos.filter(veiculo=veiculo)
        
        if (int(oficina) == 0):
            context['oficina'] = "Todas"
        else:
            context['oficina'] = Oficina.objects.get(id=oficina)
            consertos = consertos.filter(oficina=oficina)
        
        if (int(categoria) == 0):
            context['categoria'] = "Todas"
        else:
            context['categoria'] = CategoriaConserto.objects.get(id=categoria)
            consertos = consertos.filter(categoria=categoria)
        
        data_inicial = request.GET.get('from')
        data_final = request.GET.get('to')

        data_inicial, data_final = formatar_data(data_inicial, data_final)

        context['data_inicial'] = data_inicial
        context['data_final'] = data_final

        consertos = consertos.filter(data__range=(data_inicial, data_final)).order_by('data')

        total_conserto = 0
        for conserto in consertos:
            total_conserto += conserto.valor
        
        context['consertos'] = consertos
        context['total_conserto'] = total_conserto

        return render(request, 'relatorios/relatorio_conserto.html', context)
    
    return render(request, 'relatorios/index_conserto.html', context)