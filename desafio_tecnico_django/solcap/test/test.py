from django.test import TestCase
from rest_framework.test import APITestCase
from desafio_tecnico_django.solcap.models import Person
# para pegar lista de urls de acordo com o basename do router.register
#from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.test.client import Client

class PersonTestCase(APITestCase):

	def setUp(self):
		self.list_url = 'http://localhost:8000/peoples/'
		self.person1 = Person.objects.create(
					nome='Cezar Augusto',
					cpf='111.222.333-44',
					rg='11.222.333-4',
					data_nasc='1986-05-09',
					sexo='Masculino',
					mae='Graça Maria',
					pai='Castilho Mario',
					celular='(31) 99999-9999',
					altura='1.80',
					peso='80',
					tipo_sanguineo='AB+')
		self.person2 = Person.objects.create(
					nome='Marcos Willian',
					cpf='555.666.777-88',
					rg='55.666.777-8',
					data_nasc='1999-05-06',
					sexo='Masculino',
					mae='Maria Graça',
					pai='Mario Luís',
					celular='(65) 98888-7777',
					altura='1.75',
					peso='90',
					tipo_sanguineo='B+')

	#def test_to_fail(self):
	#	self.fail("Proposital fail, don't worry")

	def	test_get_peoples(self):
		"""Teste GET para verificar a requisição GET para listar as pessoas"""
		response = self.client.get(self.list_url)
		self.assertEquals(response.status_code, status.HTTP_200_OK)
	
	def	test_post_all(self):
		"""Teste POST para criar uma pessoa"""
		data = {
			'nome':'Guilhermina Vergara',
			'cpf':'123.456.789-10',
			'rg':'12.345.678-9',
			'data_nasc':'1989-07-25',
			'sexo':'Feminino',
			'mae':'Ana Vergara',
			'pai':'Pedro Vergara',
			'celular':'(98) 91234-5678',
			'altura':'1.93',
			'peso':'80',
			'tipo_sanguineo':'O+'
		}
		response = self.client.post('http://localhost:8000/all/', data=data)
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)

