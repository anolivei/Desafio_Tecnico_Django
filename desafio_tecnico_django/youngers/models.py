from django.db import models

# Create your models here.
class Person(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.IntegerField()
	rg = models.IntegerField()
