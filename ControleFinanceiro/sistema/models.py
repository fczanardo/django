# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class TipoDespesa(models.Model):
	nome = models.CharField(max_length=100)
		
	def __str__(self):
		return self.nome.decode("utf-8")

	
class Despesa(models.Model):
	tipoDespesa = models.ForeignKey(TipoDespesa)
	data = models.DateField()
	valor = models.FloatField()
	
	
class Ganho(models.Model):
	tipo = models.CharField(max_length=100)
	data = models.DateField()
	valor = models.FloatField()
	
	
class GeraRelatorio(models.Model):
	data = models.DateField()