from django.db import models
from django.core.exceptions import ValidationError

def validate_cuit(cuit):
	""" CUIT validator """
	cuit_valido = True
	if (len(cuit) != 11) or (not cuit.isdigit()):
		cuit_valido = False

	if cuit_valido:
		base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
		aux = 0
		for i in xrange(10):
			aux += int(cuit[i]) * base[i]
		aux = 11 - (aux % 11)
		if aux == 11:
			aux = 0
		elif aux == 10:
			aux = 9
		if int(cuit[10]) != aux:
			cuit_valido = False
    
	if not cuit_valido:
		raise ValidationError(u'CUIT invalido.')

class Cliente(models.Model):
	apellido = models.CharField(max_length=40)
	nombre = models.CharField(max_length=40)
	direccion = models.CharField(max_length=60)
	telefono = models.CharField(max_length=14)
	tipo_documento = models.CharField(max_length=3)
	numero_documento = models.CharField(max_length=10)
	cuit = models.CharField(max_length=13, validators=[validate_cuit])

	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellido)

class Ejercicio(models.Model):
	inicio = models.DateField()
	formato_cuenta = models.CharField(max_length=19)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return "%s %s (%d-%d)" % (self.cliente.nombre, self.cliente.apellido, self.mes_inicio, self.anho_inicio)
		
class Cuenta(models.Model):
	ejercicio = models.ForeignKey(Ejercicio)
	numero = models.CharField(max_length=6)
	nombre = models.CharField(max_length=40)
	ajuste = models.BooleanField()

	# lista_en_el_balance
	balance = models.BooleanField()

	def __unicode__(self):
		return "%s-%s" % (self.numero, self.nombre)

	##debito1  (public)
	##credito_1  (public)
	##debito_12  (public)
	##credito_12  (public)

class Asiento(models.Model):
	ejercicio = models.ForeignKey(Ejercicio)
	fecha = models.DateField()
	
RENGLON_TIPOS = (
	( 'D', 'Debito' ),
	( 'C', 'Credito' ),
)


class Renglon(models.Model):
	asiento = models.ForeignKey(Asiento)
	cuenta = models.ForeignKey(Cuenta)
	detalle = models.CharField(max_length=35)
	tipo = models.CharField(max_length=1, choices=RENGLON_TIPOS)
	importe = models.IntegerField()

	def __unicode__(self):
		return "%s %s %s %s %d" % (self.cuenta.numero, self.asiento.fecha, self.detalle, self.tipo, self.importe)
	
