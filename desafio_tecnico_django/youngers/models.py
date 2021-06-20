from django.db import models
from django.utils.translation import gettext as _

class Person(models.Model):
	nome = models.CharField(_("nome"), max_length=255)
	cpf = models.CharField(_("cpf"), max_length=20)
	rg = models.CharField(_("rg"), max_length=20)
	data_nasc = models.DateField(_("data_nasc"))
	sexo = models.CharField(_("sexo"), max_length=10)
	mae = models.CharField(_("mae"), max_length=255)
	pai = models.CharField(_("pai"), max_length=255)
	celular = models.CharField(_("celular"), max_length=20)
	altura = models.FloatField(_("altura"))
	peso = models.FloatField(_("peso"))
	tipo_sanguineo = models.CharField(_("tipo_sanguineo"), max_length=5)

def __str__(self):
	return self.nome
