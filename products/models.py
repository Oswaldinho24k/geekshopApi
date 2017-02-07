from django.db import models
#sizes
CHICA = 'CHICA'
MEDIANA = 'MEDIANA'
GRANDE = 'GRANDE'

TALLA = (
	(CHICA, 'CHICA'),
	(MEDIANA, 'MEDIANA'),
	(GRANDE, 'GRANDE')
	)

# Create your models here.
class Color(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	hexa = models.CharField(max_length=7, blank=True, null=True)
	def __str__(self):
		return self.name

class Size(models.Model):
	size = models.CharField(max_length=100, choices=TALLA, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.size


class Producto(models.Model):

	name = models.CharField(max_length=100, blank=True, null=True)
#	size = models.CharField(max_length=100, choices=TALLA, blank=True, null=True)
	colors = models.ManyToManyField(Color, related_name='colors')
	price = models.IntegerField(blank=True, null=True)
	stock = models.ManyToManyField(Size, related_name='sizes')


	def __str__(self):
		return self.name

class Imagini(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	img = models.ImageField(upload_to="imagenesproductos", blank=True, null=True)
	prod = models.ForeignKey(Producto, related_name='producto', blank=True, null=True)

	def __str__(self):
		return self.name

