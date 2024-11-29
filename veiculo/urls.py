from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'veiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/<int:pk>', views.veiculo_detalhe, name='veiculo_detalhe'),
    path('veiculo/excluir/<int:pk>', views.veiculo_excluir, name='veiculo_excluir'),
    path('veiculo/adicionar/', views.veiculo_add, name='veiculo_add'),
    path('conserto/adicionar/<int:pk>', views.conserto_add, name='conserto_add'),
    path('conserto/excluir/<int:pk>', views.conserto_excluir, name='conserto_excluir'),
    path('abastecimento/adicionar/<int:pk>', views.abastecimento_add, name='abastecimento_add'),
    path('abastecimento/excluir/<int:pk>', views.abastecimento_excluir, name='abastecimento_excluir'),
    path('oficina/adicionar', views.oficina_add, name='oficina_add'),
    path('categoria/adicionar', views.categoria_add, name='categoria_add'),
    path('posto/adicionar', views.posto_add, name='posto_add'),

    path('relatorio_veiculo/', views.index_veiculo, name='index_veiculo'),
    path('relatorio_abastecimento/', views.index_abastecimento, name='index_abastecimento'),
    path('relatorio_conserto/', views.index_conserto, name='index_conserto'),

    path('excluir_veiculo/<int:pk>/<int:args>/', views.excluir_veiculo, name='excluir_veiculo'),
    path('excluir_conserto/<int:pk>/<int:args>/', views.excluir_conserto, name='excluir_conserto'),
    path('excluir_abastecimento/<int:pk>/<int:args>/', views.excluir_abastecimento, name='excluir_abastecimento'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)