from django.test import TestCase
from rest_framework.test import APITestCase
from desafio_tecnico_django.solcap.models import Person
from django.urls import reverse

class PersonTestCase(APITestCase):
	def setUp(self):
		self.list_url = reverse('Person-list')
		self.person1 = Person.objects.create(
					nome='Cezar Augusto',
					cpf='111.222.333-44',
					rg='11.222.333-4',
					data_nasc='19/04/1986',
					sexo='Masculino',
					mae='Graça Maria',
					pai='Castilho Mario',
					celular='(31) 99999-9999',
					altura='1,80',
					peso='80',
					tipo_sanguineo='AB+')

