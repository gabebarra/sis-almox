from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Item)
admin.site.register(Unidade)
admin.site.register(Categoria)
admin.site.register(Prateleira)
admin.site.register(EntradaItem)
admin.site.register(SaidaItem)