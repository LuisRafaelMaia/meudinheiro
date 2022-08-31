from django.contrib import admin

from .models import Categoria

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    search_fields = ['nome']
    list_filter = ['nome']

admin.site.register(Categoria, CategoriaAdmin)

