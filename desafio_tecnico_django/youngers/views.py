from django.shortcuts import render
from django.http.response import HttpResponse
from desafio_tecnico_django.youngers.models import Person
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from desafio_tecnico_django.youngers.serializers import PersonSerializer
from rest_framework import viewsets

class YoungersViewSet(viewsets.ModelViewSet):
#   def list(self):
#       super
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#def youngers(request):
#    if request.method == 'GET':
#        person = Person.objects.first()
#        serializer = PersonSerializer(person)
#        return JsonResponse(serializer.data)

