from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def estoque(request):
    itens = Item.objects.all()
    context = {}
    context['itens'] = itens

    return render(request, 'estoque.html', context)

def item_detalhe(request, pk):
    itens = Item.objects.all().filter(id=pk)
    entradas = EntradaItem.objects.all().filter(item_id=pk)
    saidas = SaidaItem.objects.all().filter(item_id=pk)

    context = {}
    context['itens'] = itens
    context['entradas'] = entradas
    context['saidas'] = saidas

    return render(request, 'item_detalhe.html', context)

def entrada(request):
    entradas = EntradaItem.objects.all()
    context = {}
    context['entradas'] = entradas

    return render(request, 'entrada.html', context)

def saida(request):
    saidas = SaidaItem.objects.all()
    context = {}
    context['saidas'] = saidas

    return render(request, 'saida.html', context)

def emprestimo(request):
    saidas = SaidaItem.objects.all()
    context = {}
    context['saidas'] = saidas

    return render(request, 'emprestimo.html', context)

def item_criar(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_item");</script>' % (instance.pk, instance))
    return render(request, 'item_criar.html', {"form" : form})

def item_excluir(request, pk, args):
    if(args == 1):
        Item.objects.filter(id=pk).delete()
        return redirect('estoque:estoque')
    return redirect('estoque:estoque')

def entrada_excluir(request, pk, args):
    if(args == 1):
        EntradaItem.objects.filter(id=pk).delete()
        return redirect('estoque:entrada')
    return redirect('estoque:entrada')

def entrada_excluir_detalhe(request, pk, args):
    resp_body = '<script>window.location=document.referrer</script>' # VOLTAR P/ URL ANTERIOR

    if(args == 1):
        EntradaItem.objects.filter(id=pk).delete()
        return HttpResponse(resp_body)
    return HttpResponse(resp_body)

def saida_excluir_detalhe(request, pk, args):
    resp_body = '<script>window.location=document.referrer</script>' # VOLTAR P/ URL ANTERIOR

    if(args == 1):
        SaidaItem.objects.filter(id=pk).delete()
        return HttpResponse(resp_body)
    return HttpResponse(resp_body)

def saida_excluir(request, pk, args):
    if(args == 1):
        SaidaItem.objects.filter(id=pk).delete()
        return redirect('estoque:saida')
    return redirect('estoque:saida')

def emprestimo_excluir(request, pk, args):
    if(args == 1):
        SaidaItem.objects.filter(id=pk).delete()
        return redirect('estoque:emprestimo')
    return redirect('estoque:emprestimo')

def item_editar(request, pk):
    itens = Item.objects.all().filter(id=pk)
    padrao = {}

    for item in itens:
        padrao['nome'] = item.nome
        padrao['unidade'] = item.unidade
        padrao['prateleira'] = item.prateleira
        padrao['categoria'] = item.categoria
        padrao['estoque'] = item.estoque
        padrao['estoque_min'] = item.estoque_min
        padrao['valor'] = item.valor
        padrao['vencimento'] = item.vencimento

    form = ItemForm(request.POST or None, initial=padrao)

    if form.is_valid():
        itens.update(nome=form.cleaned_data['nome'],
                    unidade=form.cleaned_data['unidade'],
                    prateleira=form.cleaned_data['prateleira'],
                    categoria=form.cleaned_data['categoria'],
                    estoque=form.cleaned_data['estoque'],
                    estoque_min=form.cleaned_data['estoque_min'],
                    valor=form.cleaned_data['valor'],
                    vencimento=form.cleaned_data['vencimento'],)
        instance = form.save(commit=False)
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_item");</script>' % (instance.pk, instance))
    return render(request, 'item_editar.html', {"form" : form})

def entrada_item_editar(request, pk):
    entradas = EntradaItem.objects.all().filter(id=pk)
    padrao = {}

    for entrada in entradas:
        padrao['item'] = entrada.item
        padrao['funcionario'] = entrada.funcionario
        padrao['obra'] = entrada.obra
        padrao['quantidade'] = entrada.quantidade
        padrao['data'] = entrada.data
        padrao['obs'] = entrada.obs

    form = EditEntradaForm(request.POST or None, initial=padrao)

    if form.is_valid():
        entradas.update(item=form.cleaned_data['item'],
                    funcionario=form.cleaned_data['funcionario'],
                    obra=form.cleaned_data['obra'],
                    quantidade=form.cleaned_data['quantidade'],
                    data=form.cleaned_data['data'],
                    obs=form.cleaned_data['obs'])
        instance = form.save(commit=False)
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_entradaitem");</script>' % (instance.pk, instance))
    return render(request, 'entrada_editar.html', {"form" : form})

def saida_item_editar(request, pk):
    saidas = SaidaItem.objects.all().filter(id=pk)
    padrao = {}

    for saida in saidas:
        padrao['item'] = saida.item
        padrao['funcionario'] = saida.funcionario
        padrao['obra'] = saida.obra
        padrao['quantidade'] = saida.quantidade
        padrao['data'] = saida.data
        padrao['obs'] = saida.obs

    form = EditSaidaForm(request.POST or None, initial=padrao)

    if form.is_valid():
        saidas.update(item=form.cleaned_data['item'],
                    funcionario=form.cleaned_data['funcionario'],
                    obra=form.cleaned_data['obra'],
                    quantidade=form.cleaned_data['quantidade'],
                    data=form.cleaned_data['data'],
                    obs=form.cleaned_data['obs'])
        instance = form.save(commit=False)
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saidaitem");</script>' % (instance.pk, instance))
    return render(request, 'saida_editar.html', {"form" : form})

def emprestimo_editar(request, pk):
    saidas = SaidaItem.objects.all().filter(id=pk)
    padrao = {}

    for saida in saidas:
        padrao['item'] = saida.item
        padrao['funcionario'] = saida.funcionario
        padrao['obra'] = saida.obra
        padrao['quantidade'] = saida.quantidade
        padrao['data'] = saida.data
        padrao['obs'] = saida.obs

    form = EditSaidaForm(request.POST or None, initial=padrao)

    if form.is_valid():
        saidas.update(item=form.cleaned_data['item'],
                    funcionario=form.cleaned_data['funcionario'],
                    obra=form.cleaned_data['obra'],
                    quantidade=form.cleaned_data['quantidade'],
                    data=form.cleaned_data['data'],
                    obs=form.cleaned_data['obs'])
        instance = form.save(commit=False)
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_emprestimo");</script>' % (instance.pk, instance))
    return render(request, 'emprestimo_editar.html', {"form" : form})


def item_entrada(request):
    form = EntradaForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_entrada_item");</script>' % (instance.pk, instance))
    return render(request, 'item_entrada.html', {"form" : form})

def item_saida(request):
    form = SaidaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.emprestimo = False
        instance = form.save()

        if request.FILES:
            for f in request.FILES.getlist('files'):
                obj = FotosSaida.objects.create(foto=f, saida_id=instance.id)
            SaidaItem.objects.filter(id=instance.id).update(galeria = True)

        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saida_item");</script>' % (instance.pk, instance))
    return render(request, 'item_saida.html', {"form" : form})

def item_emprestimo(request):
    form = SaidaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.emprestimo = True
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saida_item");</script>' % (instance.pk, instance))
    return render(request, 'item_emprestimo.html', {"form" : form})

def entrada_unica(request, pk):
    itens = Item.objects.filter(id=pk)
    nome = ""

    form = EntradaUnicaForm(request.POST or None)

    for item in itens:
        nome = item.nome
    
    context = {}
    context['itens'] = itens
    context['nome'] = nome
    context['form'] = form

    if form.is_valid():
        instance = form.save(commit=False)
        instance.item_id = pk
        instance = form.save()
        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_entrada_item");</script>' % (instance.pk, instance))
    return render(request, 'entrada_unica.html', context)

def saida_unica(request, pk):
    itens = Item.objects.filter(id=pk)
    nome = ""

    form = SaidaUnicaForm(request.POST or None)

    for item in itens:
        nome = item.nome
    
    context = {}
    context['itens'] = itens
    context['nome'] = nome
    context['form'] = form

    if form.is_valid():
        instance = form.save(commit=False)
        instance.item_id = pk
        instance.emprestimo = False
        instance = form.save()

        if request.FILES:
            for f in request.FILES.getlist('files'):
                obj = FotosSaida.objects.create(foto=f, saida_id=instance.id)
            SaidaItem.objects.filter(id=instance.id).update(galeria = True)

        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saida_item");</script>' % (instance.pk, instance))
    return render(request, 'saida_unica.html', context)

def add_unidade(request):
    form = UnidadeForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_unidade");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_unidade.html', context)

def add_prateleira(request):
    form = PrateleiraForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_prateleira");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_prateleira.html', context)

def add_categoria(request):
    form = CategoriaForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_categoria");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_categoria.html', context)

def add_item(request):
    form = ItemForm(request.POST or None)
    context = {}
    context['form'] = form
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup_NoRefresh(window, "%s", "%s", "#id_item");</script>' % (instance.pk, instance))
    return render(request, 'separate/add_item.html', context)

def emprestimo_add(request, pk):
    form = EmprestimoUnicoForm(request.POST or None)
    itens = Item.objects.all().filter(id=pk)
    nome = ""

    for item in itens:
        nome = item.nome

    context = {}
    context['nome'] = nome
    context['form'] = form

    if form.is_valid():
        instance = form.save(commit=False)
        instance.item_id = pk
        instance.emprestimo = True
        instance = form.save()

        if request.FILES:
            for f in request.FILES.getlist('files'):
                obj = FotosSaida.objects.create(foto=f, saida_id=instance.id)
            SaidaItem.objects.filter(id=instance.id).update(galeria = True)

        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saida_item");</script>' % (instance.pk, instance))
    return render(request, 'emprestimo_add.html', context)

def emprestimo_add_funcionario(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    inicial = {}
    inicial['funcionario'] = funcionario

    form = SaidaForm(request.POST or None, initial=inicial)

    context = {}
    context['form'] = form

    if form.is_valid():
        instance = form.save(commit=False)
        instance.emprestimo = True
        instance = form.save()
        
        if request.FILES:
            for f in request.FILES.getlist('files'):
                obj = FotosSaida.objects.create(foto=f, saida_id=instance.id)
            SaidaItem.objects.filter(id=instance.id).update(galeria = True)

        if(request.POST.get('add')):
            return HttpResponse('<script>window.location.href = window.location.href</script>')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_saida_item");</script>' % (instance.pk, instance))
    return render(request, 'emprestimo_add_funcionario.html', context)

def emprestimo_devolver(request, pk):
    inicial = {}
    context = {}

    saida = SaidaItem.objects.get(id=pk)
    inicial['quantidade'] = saida.quantidade
    context['item'] = saida.item.nome

    form = EmprestimoDevolverForm(request.POST or None, initial=inicial)
    context['form'] = form

    if form.is_valid(): # VAI CRIAR UMA ENTRADA BASEADA NA DEVOLUÇÃO, E TBM UMA NOVA SAIDA SE NÃO DEVOLVER TOTAL
        instance = form.save(commit=False)
        instance.emprestimo = True
        instance.funcionario = saida.funcionario
        instance.obra = saida.obra

        if (form.cleaned_data['obs']): # COLOCAR UM ['D'] ANTES DE QUALQUER CAMPO DE OBS P/ IDENTIFICAR Q É UMA DEVOLUÇÃO
            instance.obs = "[D] " + form.cleaned_data['obs']
        else:
            instance.obs = "[D]"
        instance.item = saida.item

        SaidaItem.objects.filter(id=pk).update(
            entregue = True,
            devolucao = instance.data,
        )

        quantidade_devolucao = saida.quantidade - instance.quantidade

        if (instance.quantidade < saida.quantidade): # CORRIGINDO O ESTOQUE
            nova_saida = SaidaItem.objects.create( # Cria uma nova saida com o restante que o funcionário está devendo
                item = saida.item,
                emprestimo = True,
                entregue = False,
                quantidade = 0, # VALOR DE 0 PARA NÃO EXTRAIR DO ESTOQUE
                data = instance.data,
                obs = "Pendência " + str(instance.data.strftime("%d/%m/%Y")),
                funcionario = saida.funcionario,
                obra = saida.obra,
            )
            SaidaItem.objects.filter(id=nova_saida.id).update(quantidade=quantidade_devolucao) # ALTERANDO O CAMPO DE 0 P/ RESTANTE, SEM 
        
        if(saida.item.categoria.categoria == 'EPI'): # SE FOR EPI, NÃO CRIA A ENTRADA, PQ EPI NÃO VOLTA PRO ESTOQUE
            instance = form.save(commit=False)
        else:
            instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_item");</script>' % (instance.pk, instance))


    return render(request, 'emprestimo_devolver.html', context)

def emprestimo_substituir(request, pk):
    context = {}

    hoje = date.today()

    saida = SaidaItem.objects.get(id=pk)


    form = EmprestimoSubstituirForm(request.POST or None)
    context['form'] = form
    context['item'] = saida.item.nome

    if form.is_valid():
        # ------ CRIANDO NOVO EMPRÉSTIMO -------
        instance = form.save(commit=False)

        if (form.cleaned_data['obs']): # COLOCAR UM ['D'] ANTES DE QUALQUER CAMPO DE OBS P/ IDENTIFICAR Q É UMA DEVOLUÇÃO
            instance.obs = "[Substituição] " + form.cleaned_data['obs']
        else:
            instance.obs = "[Substituição]"
        
        instance.emprestimo = True
        instance.entregue = False
        instance.item = saida.item
        instance.quantidade = 0
        instance.data = hoje
        if saida.funcionario:
            instance.funcionario = saida.funcionario
        if saida.obra:
            instance.obra = saida.obra

        instance = form.save()

        # -------- ATUALIZANDO EMPRÉSTIMO ATUAL ------
        SaidaItem.objects.filter(id=pk).update(
            entregue = True,
            devolucao = hoje,
        )

        SaidaItem.objects.filter(id=instance.id).update(
            quantidade = saida.quantidade
        )

        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#epis_tab");</script>' % (instance.pk, instance))
    return render(request, 'emprestimo_substituir.html', context)
        
def fotos_saida(request, pk):
    fotos = FotosSaida.objects.all().filter(saida_id=pk)
    context = {}
    context['fotos'] = fotos
    return render(request, 'galeria_saida.html', context)

