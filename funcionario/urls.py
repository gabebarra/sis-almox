from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'funcionario'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/<int:pk>', views.funcionario_detalhe, name='funcionario_detalhe'),
    path('adicionar', views.funcionario_add, name='funcionario_add'),
    path('adicionar_norefresh', views.funcionario_add_norefresh, name='funcionario_add_norefresh'),
    path('funcao/adicionar', views.funcao_add, name='funcao_add'),
    path('empresa/adicionar', views.empresa_add, name='empresa_add'),

    path('add_funcionario/', views.add_funcionario, name='add_funcionario'),
    path('editar/<int:pk>', views.edit_funcionario, name='edit_funcionario'),
    path('teste/', views.formset_funcionario, name='formset_funcionario'),
    path('excluir_funcionario/<int:pk>/<int:args>/', views.funcionario_excluir, name='funcionario_excluir'),

    path('relatorio_funcionario/<int:pk>', views.index_funcionario, name='index_funcionario'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)