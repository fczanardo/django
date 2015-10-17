# -*- coding: utf-8 -*-
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'sistema.views.lista'),

	
	(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html' }),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login',{'login_url': '/login/'}),
		
	# Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	
	(r'^adicionaTipoDespesa/$', 'sistema.views.adicionaTipoDespesa'),
	(r'^adicionaDespesa/$', 'sistema.views.adicionaDespesa'),
	(r'^adicionaGanho/$', 'sistema.views.adicionaGanho'),
	
	(r'^listaTipoDespesa/$', 'sistema.views.listaTipoDespesa'),
	(r'^listaDespesa/$', 'sistema.views.listaDespesa'),
	(r'^listaGanho/$', 'sistema.views.listaGanho'),
	
	(r'^removeTipoDespesa/(?P<nr_item>\d+)/$', 'sistema.views.removeTipoDespesa'),
	(r'^removeDespesa/(?P<nr_item>\d+)/$', 'sistema.views.removeDespesa'),
	(r'^removeGanho/(?P<nr_item>\d+)/$', 'sistema.views.removeGanho'),
	
	(r'^itemTipoDespesa/(?P<nr_item>\d+)/$', 'sistema.views.itemTipoDespesa'),
	(r'^itemDespesa/(?P<nr_item>\d+)/$', 'sistema.views.itemDespesa'),
	(r'^itemGanho/(?P<nr_item>\d+)/$', 'sistema.views.itemGanho'),
	
	(r'^graficoComparativoTela/', 'sistema.views.graficoComparativoTela'),
	(r'^graficoComparativo/(?P<dateFilter>\d+)/', 'sistema.views.graficoComparativo'),
)
