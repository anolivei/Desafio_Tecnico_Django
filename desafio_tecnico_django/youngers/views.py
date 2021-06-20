from desafio_tecnico_django.youngers.models import Person
from desafio_tecnico_django.youngers.serializers import PersonSerializer
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect

def youngers(request):
    num = request.GET.get('num')
    return num

class YoungersViewSet(viewsets.ModelViewSet):
    num = 5
    queryset = Person.objects.order_by("-data_nasc")[:num]
    serializer_class = PersonSerializer
