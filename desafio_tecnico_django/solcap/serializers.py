from rest_framework import serializers
from desafio_tecnico_django.solcap.models import Person, Blood, Gender

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = [  'id',
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
					'tipo_sanguineo'
					]

class BloodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blood
		fields = [	'tipo_sanguineo',
					'frequencia'
					]

class GenderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gender
		fields = [	'sexo',
					'porcentagem'
					]