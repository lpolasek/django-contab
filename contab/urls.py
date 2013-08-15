from django.conf.urls import patterns, include, url
from contab import models, forms

clientes_parameters = {'model': models.Cliente, 'url_base': 'clientes', 'form': forms.Cliente }
ejercicios_parameters = {'model': models.Ejercicio, 'url_base': 'ejercicios', 'form': forms.Ejercicio }

urlpatterns = patterns('contab.views',
    url(r'^$', 'list', clientes_parameters),
    url(r'^clientes/$', 'list', clientes_parameters, name='clientes'),    
    url(r'^clientes/add/$', 'add', clientes_parameters, name='clientes_add' ),
    url(r'^clientes/edit/(?P<model_id>\d+)/$', 'edit', clientes_parameters, name='clientes_edit' ),
    url(r'^clientes/delete/(?P<model_id>\d+)/$', 'delete', clientes_parameters, name='clientes_delete' ),

    url(r'^(?P<cliente_id>\d+)/ejercicios/$', 'ejercicios_list', ejercicios_parameters, name='ejercicios' ),

    url(r'^(?P<cliente_id>\d+)/ejercicios/add/$', 'ejercicios_add', ejercicios_parameters, name='ejercicios_add' ),
    url(r'^(?P<cliente_id>\d+)/ejercicios/edit/(?P<model_id>\d+)/$', 'ejercicios_edit', ejercicios_parameters, name='ejercicios_edit' ),
    url(r'^(?P<cliente_id>\d+)/ejercicios/delete/(?P<model_id>\d+)/$', 'ejercicios_delete', ejercicios_parameters, name='ejercicios_delete' ),   
)


