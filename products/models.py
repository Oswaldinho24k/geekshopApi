from django.db import models
CHICA = 'CHICA'
MEDIANA = 'MEDIANA'
GRANDE = 'GRANDE'

TALLA = (
	(CHICA, 'CHICA'),
	(MEDIANA, 'MEDIANA'),
	(GRANDE, 'GRANDE')
	)
# Create your models here.
class Producto(models.Model):

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="imagenesproductos")
	size = models.CharField(max_length=100, choices=TALLA)
	color = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.IntegerField()

	def __str__(self):
		return self.name




