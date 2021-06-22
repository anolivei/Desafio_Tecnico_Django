from desafio_tecnico_django.solcap.models import Person
from desafio_tecnico_django.solcap.serializers import PersonSerializer, BloodSerializer, GenderSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

class AllViewSet(viewsets.ModelViewSet):
	"""Listando todas as pessoas em ordem de id"""
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class Youngers(generics.ListAPIView):
	"""Listando as pessoas em ordem crescente de idade"""
	queryset = Person.objects.all().order_by("-data_nasc")
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class YoungersFilter(generics.ListAPIView):
	"""Listando n pessoas mais novas"""
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("-data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class Olders(generics.ListAPIView):
	"""Listando as pessoas em ordem decrescente de idade"""
	queryset = Person.objects.all().order_by("data_nasc")
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class OldersFilter(generics.ListAPIView):
	"""Listando n pessoas mais velhas"""
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class Peoples(generics.ListAPIView):
	"""Listando as pessoas em ordem alfabética"""
	queryset = Person.objects.all().order_by("nome")
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class ListByCpf(generics.ListAPIView):
	"""Retorna dados de uma pessoa de acordo com o CPF"""
	def get_queryset(self):
		num = self.kwargs['pk']
		if len(num) < 11:
			num = num.zfill(11)
		num = '{}.{}.{}-{}'.format(num[:3], num[3:6], num[6:9], num[9:])
		queryset = Person.objects.filter(cpf=num)
		return queryset
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class PeoplesSearch(generics.ListAPIView):
	"""Retorna dados de uma pessoa de acordo com o nome ou parte do nome"""
	def get_queryset(self):
		search = self.kwargs['pk']
		queryset = Person.objects.filter(nome__contains=search)
		return queryset
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class Blood(generics.ListAPIView):
	"""Listando frequencias dos tipos sanguineos"""
	def get_queryset(self):
		queryset = (Person.objects
			.values('tipo_sanguineo')
			.annotate(frequencia=Count('tipo_sanguineo'))
			.order_by('frequencia'))
		return queryset
	serializer_class = BloodSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class ListByBloodType(generics.ListAPIView):
	"""Listando as pessoas de um tipo sanguineo"""
	def get_queryset(self):
		queryset = Person.objects.filter(tipo_sanguineo=self.kwargs['pk'])
		return queryset
	serializer_class = PersonSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]

class Gender(generics.ListAPIView):
	"""Listando porcentagem dos gêneros"""
	def get_queryset(self):
		total = Person.objects.all().count()
		queryset = (Person.objects
			.values('sexo')
			.annotate(porcentagem=Count('sexo') * 100/total)
			.order_by('porcentagem'))
		return queryset
	serializer_class = GenderSerializer
	#authentication_classes = [BasicAuthentication]
	#permission_classes = [IsAuthenticated]