from django import forms
from contab import models
from crispy_forms.helper import FormHelper

class Cliente(forms.ModelForm):
        class Meta:
                model = models.Cliente

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.help_text_inline = False
		
		super(Cliente, self).__init__(*args, **kwargs)
		
class Ejercicio(forms.ModelForm):
        class Meta:
                model = models.Ejercicio
		widgets = {
#			'inicio': forms.DateInput(format='%Y-%m-%d'),
			'cliente': forms.HiddenInput() }

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.help_text_inline = False
		
		super(Ejercicio, self).__init__(*args, **kwargs)