from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from models import *

def list(request, model, url_base, form):
	empty_form = form()
	items = model.objects.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': empty_form, 'action': reverse('%s_add' % url_base), 'button_label': 'Agregar',  }, 
	)

def add(request, model, url_base, form):
	new_model = form()
	if request.method == 'POST':
		new_model = form(request.POST)
		if new_model.is_valid():
			new_model.save()
			return redirect(reverse(url_base))

	items = model.objects.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': new_model, 'action': reverse("%s_add" % url_base), 'button_label': 'Agregar',  }, 
	)

def delete(request, model, url_base, model_id, form):
	item = get_object_or_404(model, pk=model_id)
	item.delete()
	template_name = '%s_list.html' % url_base.lower()
	return redirect(reverse(url_base))

def edit(request, model, url_base, form, model_id):
	item = get_object_or_404(model, pk=model_id)
	edit_form = form(request.POST or None, instance=item)
	if edit_form.is_valid():
		item = edit_form.save()
		item.save()
		return redirect(reverse(url_base))

	items = model.objects.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': edit_form, 'action': reverse("%s_edit" % url_base,  kwargs={ 'model_id': model_id }), 'button_label': 'Actualizar'}, 
	)

def ejercicios_list(request, model, cliente_id, url_base, form):
	cliente = get_object_or_404(Cliente, pk=cliente_id)
	empty_form = form(initial={'cliente': cliente.pk})
	items = cliente.ejercicio_set.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': empty_form, 'action': reverse('%s_add' % url_base, kwargs={ 'cliente_id': cliente_id }), 'button_label': 'Agregar', 'cliente': cliente, }, 
	)
	
def ejercicios_add(request, model, cliente_id, url_base, form):
	cliente = get_object_or_404(Cliente, pk=cliente_id)
	new_model = form(initial={'cliente': cliente.pk})
	if request.method == 'POST':
		new_model = form(request.POST)
		if new_model.is_valid():
			new_model.save()
			return redirect(reverse(url_base, kwargs={ 'cliente_id': cliente_id }))

	items = cliente.ejercicio_set.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': new_model, 'action': reverse("%s_add" % url_base, kwargs={ 'cliente_id': cliente_id }), 'button_label': 'Agregar', 'cliente': cliente, }, 
	)
	
def ejercicios_delete(request, model, cliente_id, url_base, model_id, form):
	cliente = get_object_or_404(Cliente, pk=cliente_id)
	item = get_object_or_404(model, pk=model_id)
	item.delete()
	template_name = '%s_list.html' % url_base.lower()
	return redirect(reverse(url_base, kwargs={ 'cliente_id': cliente_id }))

def ejercicios_edit(request, model, cliente_id, url_base, form, model_id):
	item = get_object_or_404(model, pk=model_id)
	cliente = get_object_or_404(Cliente, pk=cliente_id)
	edit_form = form(request.POST or None, instance=item)
	if edit_form.is_valid():
		item = edit_form.save()
		item.save()
		return redirect(reverse(url_base, kwargs={ 'cliente_id': cliente_id }))

	items = cliente.ejercicio_set.all()
	template_name = '%s_list.html' % url_base
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': edit_form, 'action': reverse("%s_edit" % url_base,  kwargs={ 'cliente_id':cliente.id, 'model_id': model_id }), 'button_label': 'Actualizar', 'cliente': cliente, }, 
	)