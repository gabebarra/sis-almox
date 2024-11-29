from django.urls import path
from . import views
from . import invoice_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'estoque'

urlpatterns = [
    path('', views.estoque, name='estoque'),
    path('detalhe/<int:pk>', views.item_detalhe, name='item_detalhe'),
    path('entrada/', views.entrada, name='entrada'),
    path('criar/', views.item_criar, name='item_criar'),
    path('editar/<int:pk>', views.item_editar, name='item_editar'),
    path('entrada_editar/<int:pk>', views.entrada_item_editar, name='entrada_item_editar'),
    path('saida_editar/<int:pk>', views.saida_item_editar, name='saida_item_editar'),
    path('emprestimo_editar/<int:pk>', views.emprestimo_editar, name='emprestimo_editar'),

    path('item_entrada/', views.item_entrada, name='item_entrada'),
    path('item_saida/', views.item_saida, name='item_saida'),
    path('item_emprestimo/', views.item_emprestimo, name='item_emprestimo'),
    
    path('excluir/<int:pk>/<int:args>/', views.item_excluir, name='item_excluir'),
    path('excluir_entrada/<int:pk>/<int:args>/', views.entrada_excluir, name='entrada_excluir'),
    path('excluir_entrada_detalhe/<int:pk>/<int:args>/', views.entrada_excluir_detalhe, name='entrada_excluir_detalhe'),

    path('excluir_saida/<int:pk>/<int:args>/', views.saida_excluir, name='saida_excluir'),
    path('excluir_saida_detalhe/<int:pk>/<int:args>/', views.saida_excluir_detalhe, name='saida_excluir_detalhe'),
    path('excluir_emprestimo/<int:pk>/<int:args>/', views.emprestimo_excluir, name='emprestimo_excluir'),
    path('entrada/<int:pk>', views.entrada_unica, name='entrada_unica'),
    path('saida/<int:pk>', views.saida_unica, name='saida_unica'),
    path('saida/', views.saida, name='saida'),

    path('saida/galeria/<int:pk>', views.fotos_saida, name='fotos_saida'),


    path('emprestimo/', views.emprestimo, name='emprestimo'),
    path('emprestimo_substituir/<int:pk>', views.emprestimo_substituir, name='emprestimo_substituir'),
    path('emprestimo/<int:pk>', views.emprestimo_add, name='emprestimo_add'),
    path('emprestimo/funcionario/<int:pk>', views.emprestimo_add_funcionario, name='emprestimo_add_funcionario'),
    path('emprestimo_devolver/<int:pk>', views.emprestimo_devolver, name='emprestimo_devolver'),

    path('add_item/', views.add_item, name='add_item'),
    path('add_unidade/', views.add_unidade, name='add_unidade'),
    path('add_categoria/', views.add_categoria, name='add_categoria'),
    path('add_prateleira/', views.add_prateleira, name='add_prateleira'),

    path('relatorio_estoque/', invoice_views.index_estoque, name='index_estoque'),
    path('relatorio_saida/', invoice_views.index_saida, name='index_saida'),
    path('relatorio_emprestimo/', invoice_views.index_emprestimo, name='index_emprestimo'),
    path('relatorio_entrada/', invoice_views.index_entrada, name='index_entrada'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)