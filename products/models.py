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
	color = models.CharField(max_length=100)
	def __str__(self):
		return self.color

class Size(models.Model):
	size = models.CharField(max_length=100, choices=TALLA)
	quantity = models.IntegerField()

	def __str__(self):
		return self.size

class Producto(models.Model):

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="imagenesproductos")
#	size = models.CharField(max_length=100, choices=TALLA)
	color = models.ManyToManyField(Color, related_name='colors')
	price = models.IntegerField()
	stock = models.ManyToManyField(Size, related_name='sizes')

	def __str__(self):
		return self.name




