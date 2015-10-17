# -*- coding: utf-8 -*-

from django import forms
from sistema.models import TipoDespesa, Despesa, Ganho, GeraRelatorio
from django.contrib.auth.models import User


class ModelMultipleUserField(forms.ModelMultipleChoiceField):
	def label_from_instance(self, user):
		return u"%s (%s)" % (use.getNome(), user)
		
		
class FormTipoDespesa(forms.ModelForm):
	class Meta:
		model = TipoDespesa
		fields = ('nome' ,)
		

class FormDespesa(forms.ModelForm):
	data = forms.DateField(
		widget=forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%Y', '%d/%m/%y'])

	class Meta: 
		model = Despesa
		fields = ('tipoDespesa', 'data', 'valor' )
		
		
class FormGanho(forms.ModelForm):
	data = forms.DateField(
		widget=forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%Y', '%d/%m/%y'])
		
	class Meta:
		model = Ganho
		fields = ('tipo', 'data', 'valor', )	


class FormGeraGraficoComparativo(forms.ModelForm):
	data = forms.DateField(
		widget=forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%Y', '%d/%m/%y'])
		
	class Meta:
		model = GeraRelatorio
		fields = ('data', )	