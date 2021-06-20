from rest_framework import authentication
from desafio_tecnico_django.youngers import serializers
from desafio_tecnico_django.youngers.models import Person
from desafio_tecnico_django.youngers.serializers import PersonSerializer
from rest_framework import viewsets, generics
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class AllViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class YoungersViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all().order_by("-data_nasc")
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]
class YoungersFilter(generics.ListAPIView):
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("-data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class OldersViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all().order_by("data_nasc")
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class OldersFilter(generics.ListAPIView):
	def get_queryset(self):
		num = self.kwargs['pk']
		queryset = Person.objects.all().order_by("data_nasc")[:num]
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

class ListaTipoSangue(generics.ListAPIView):
	"""Listando as pessoas de um tipo sanguineo"""
	def get_queryset(self):
		queryset = Person.objects.filter(tipo_sanguineo=self.kwargs['pk'])
		return queryset
	serializer_class = PersonSerializer
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]

