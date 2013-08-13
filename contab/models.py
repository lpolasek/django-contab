from django.db import models

class Cliente(models.Model):
	apellido = models.CharField(max_length=40)
	nombre = models.CharField(max_length=40)
	direccion = models.CharField(max_length=60)
	telefono = models.CharField(max_length=14)
	tipo_documento = models.CharField(max_length=3)
	numero_documento = models.CharField(max_length=10)
	cuit = models.CharField(max_length=13)

	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellido)

class Ejercicio(models.Model):
	mes_inicio = models.PositiveSmallIntegerField()
	anho_inicio = models.PositiveSmallIntegerField()
	formato_cuenta = models.CharField(max_length=19)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return "%s %s (%d-%d)" % (self.cliente.nombre, self.cliente.apellido, self.mes_inicio, self.anho_inicio)
		
#class Cuenta(models.Model):
	#nro_cuenta  (public)
	#nombre_cuenta  (public)
	#ajuste  (public)
	
	## lista_en_el_balance
	#balance (public)
	##debito1  (public)
	##credito_1  (public)
	##debito_12  (public)
	##credito_12  (public)
