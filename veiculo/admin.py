from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Veiculo)
admin.site.register(Posto)
admin.site.register(Abastecimento)
admin.site.register(CategoriaConserto)
admin.site.register(Oficina)
admin.site.register(Conserto)