# -*- coding: utf-8 -*-

from models import TipoDespesa, Despesa, Ganho
from django.shortcuts import render
from forms import FormTipoDespesa, FormDespesa , FormGanho, FormGeraGraficoComparativo
from django.shortcuts import render_to_response, get_object_or_404, redirect, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def lista(request):
	return render(request, "lista.html")

	
@login_required
def listaTipoDespesa(request):
	lista_itens = TipoDespesa.objects.all()
	return render(request, "listaTipoDespesa.html", {'lista_itens': lista_itens})

	
@login_required
def listaDespesa(request):
	lista_itens = Despesa.objects.all()
	return render(request, "listaDespesa.html", {'lista_itens': lista_itens})
	
	
@login_required
def listaGanho(request):
	lista_itens = Ganho.objects.all()
	return render(request, "listaGanho.html", {'lista_itens': lista_itens})
	
	
@login_required
def itemTipoDespesa(request, nr_item):
	item = get_object_or_404(TipoDespesa, pk=nr_item)
	form = FormTipoDespesa(request.POST or None, request.FILES or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect("/listaTipoDespesa/")
	return render(request, "item.html", {'form': form})
	

@login_required
def itemDespesa(request, nr_item):
	item = get_object_or_404(Despesa, pk=nr_item)
	form = FormDespesa(request.POST or None, request.FILES or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect("/listaDespesa/")
	return render(request, "item.html", {'form': form})
	
	
@login_required
def itemGanho(request, nr_item):
	item = get_object_or_404(Ganho, pk=nr_item)
	form = FormGanho(request.POST or None, request.FILES or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect("/listaGanho/")
	return render(request, "item.html", {'form': form})
	
	
@login_required
def removeTipoDespesa(request, nr_item):
	item = get_object_or_404(TipoDespesa, pk=nr_item)
	if request.method == "POST":
		item.delete()
		return redirect("/listaTipoDespesa/")
	return render(request, "removeTipoDespesa.html", {'item': item})
	
	
@login_required
def removeDespesa(request, nr_item):
	item = get_object_or_404(Despesa, pk=nr_item)
	if request.method == "POST":
		item.delete()
		return redirect("/listaDespesa/")
	return render(request, "removeDespesa.html", {'item': item})
	
	
@login_required
def removeGanho(request, nr_item):
	item = get_object_or_404(Ganho, pk=nr_item)
	if request.method == "POST":
		item.delete()
		return redirect("/listaGanho/")
	return render(request, "removeGanho.html", {'item': item})
	

@login_required	
def adicionaTipoDespesa(request):
	form = FormTipoDespesa(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		form.save()
		return redirect("/")
	
	return render(request, "adicionaTipoDespesa.html", {'form': form})
    
	
@login_required	
def adicionaDespesa(request):
	form = FormDespesa(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		form.save()
		return redirect("/")
	
	return render(request, "adicionaDespesa.html", {'form': form})
	
	
@login_required	
def adicionaGanho(request):
	form = FormGanho(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		form.save()
		return redirect("/")
	
	return render(request, "adicionaGanho.html", {'form': form})
	
	
@login_required
def graficoComparativoTela(request):
	form = FormGeraGraficoComparativo(request.POST or None, request.FILES or None)
	
	if form.is_valid():
		aux = form.cleaned_data
		field = aux['data']
		import string
		value = string.replace(str(field), '-', '')
		return redirect(graficoComparativo, dateFilter = value)
	return render(request, "graficoComparativo.html",{'form' : form })
	
	
@login_required
def graficoComparativo(request,dateFilter):

	valorFiltroAno = dateFilter[:4]
	valorFiltroMes = dateFilter[4:-2]
	
	print valorFiltroAno
	print valorFiltroMes

	ganhoList = Ganho.objects.filter(data__year=int(valorFiltroAno) ,data__month=int(valorFiltroMes) )
	despesaList = Despesa.objects.filter(data__year=int(valorFiltroAno) ,data__month=int(valorFiltroMes) )
	
	acumuladorGanho = 0
	acumuladorDespesa = 0
	
	for item in ganhoList:
		acumuladorGanho += item.valor
		
	for item in despesaList:
		acumuladorDespesa += item.valor

	#instancia o objeto de desenho
	import mycharts
	d = mycharts.MyBarChartDrawing()

	d.chart.data = [(0,acumuladorDespesa,0),(0,acumuladorGanho,0)]

	extensaoGraficoParaValor = d.chart.width - 60
	localizacaoValorGanho = 0
	localizacaoValorDespsa = 0
	
	if acumuladorGanho > acumuladorDespesa:
		localizacaoValorGanho = extensaoGraficoParaValor
		localizacaoValorDespesa = (acumuladorDespesa * d.chart.width / acumuladorGanho) - 60
	else:
		if acumuladorDespesa > acumuladorGanho:
			localizacaoValorDespesa = extensaoGraficoParaValor
			localizacaoValorGanho = (acumuladorGanho * d.chart.width / acumuladorDespesa) - 60
		else:
			localizacaoValorGanho = extensaoGraficoParaValor
			localizacaoValorDespesa = extensaoGraficoParaValor
	
	from reportlab.graphics.shapes import String
	d.add(String(localizacaoValorGanho,200,'R$'+str(acumuladorGanho)), name='ganhoValor')
	d.add(String(localizacaoValorDespesa,150,'R$'+str(acumuladorDespesa)), name='despesaValor')
	d.ganhoValor.fontSize = 15
	d.despesaValor.fontSize = 15
	
	binaryStuff = d.asString('gif')
	return HttpResponse(binaryStuff, 'image/gif')