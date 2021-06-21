from desafio_tecnico_django.youngers.models import Person
from desafio_tecnico_django.youngers.serializers import PersonSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.http import HttpResponse

class AllViewSet(viewsets.ModelViewSet):
	"""Listando todas as pessoas em ordem de id"""
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class Youngers(generics.ListAPIView):
	"""Listando as pessoas em ordem crescente de idade"""
	queryset = Person.objects.all().order_by("-data_nasc")
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class YoungersFilter(generics.ListAPIView):
	"""Listando n pessoas mais novas"""
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("-data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class Olders(generics.ListAPIView):
	"""Listando as pessoas em ordem decrescente de idade"""
	queryset = Person.objects.all().order_by("data_nasc")
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class OldersFilter(generics.ListAPIView):
	"""Listando n pessoas mais velhas"""
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class Peoples(generics.ListAPIView):
	"""Listando as pessoas em ordem alfabética"""
	queryset = Person.objects.all().order_by("nome")
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

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
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class Blood(generics.ListAPIView):
	def get_result():
		blood = (Person.objects
			.values('tipo_sanguineo')
			.annotate(frequency=Count('tipo_sanguineo'))
			.order_by())
		return HttpResponse('blood')
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class ListByBloodType(generics.ListAPIView):
	"""Listando as pessoas de um tipo sanguineo"""
	def get_queryset(self):
		queryset = Person.objects.filter(tipo_sanguineo=self.kwargs['pk'])
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

