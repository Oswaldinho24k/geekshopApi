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

	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to="imagenesproductos")
	talla = models.CharField(max_length=100, choices=TALLA)
	color = models.CharField(max_length=100)
	precio = models.IntegerField()
	stock = models.IntegerField()

	def __str__(self):
		return self.nombre




