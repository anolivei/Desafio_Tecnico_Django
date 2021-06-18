from rest_framework import serializers
from desafio_tecnico_django.youngers.models import Person

class PersonSerializer(serializers.ModelSerializer):
#    age = serializers.SerializerMethodField
    class Meta:
        model = Person
        fields = ['nome',
                    'cpf',
                    'rg',
                    'data_nasc',
                    'sexo',
                    'mae',
                    'pai',
                    'celular',
                    'altura',
                    'peso',
                    'tipo_sanguineo'
                    ]

#def age(self):