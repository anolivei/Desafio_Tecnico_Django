from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def youngers(request):
    if request.method == 'GET':
        return HttpResponse("hello world!")