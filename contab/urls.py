from django.conf.urls import patterns, include, url
from contab import models, forms

clientes_parameters = {'model': models.Cliente, 'url_base': 'clientes', 'form': forms.Cliente }

urlpatterns = patterns('contab.views',
    url(r'^$', 'list', clientes_parameters),
    url(r'^clientes/$', 'list', clientes_parameters, name='clientes'),    
    url(r'^clientes/add/$', 'add', clientes_parameters, name='clientes_add' ),
    url(r'^clientes/edit/(?P<model_id>\d+)/$', 'edit', clientes_parameters, name='clientes_edit' ),
    url(r'^clientes/delete/(?P<model_id>\d+)/$', 'delete', clientes_parameters, name='clientes_delete' ),
    
)


