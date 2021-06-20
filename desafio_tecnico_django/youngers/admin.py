from django.contrib import admin
from desafio_tecnico_django.youngers.models import Person

class People(admin.ModelAdmin):
    list_display = ('id',
                    'nome',
                    'cpf',
                    'rg',
                    'data_nasc',
                    'sexo',
                    'mae',
                    'pai',
                    'celular',
                    'altura',
                    'peso',
                    'tipo_sanguineo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Person, People)