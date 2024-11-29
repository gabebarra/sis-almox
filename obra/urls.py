from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'obra'

urlpatterns = [
    path('', views.index, name='index'),
    path('obra/<int:pk>', views.obra_detalhe, name='obra_detalhe'),
    path('add/', views.obra_add, name='obra_add'),

    path('add_cliente/', views.add_cliente, name='add_cliente'),

    path('add_obra/', views.add_obra, name='add_obra'),
    path('excluir_obra/<int:pk>/<int:args>/', views.obra_excluir, name='obra_excluir'),

    path('relatorio_obra/<int:pk>/', views.index_obra, name='index_obra'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)