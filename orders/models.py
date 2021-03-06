from django.db import models
from django.contrib.auth.models import User
from products.models import Producto


# Create your models here.

class Order(models.Model):
	user=models.OneToOneField(User, blank=True, null=True)
	cname = models.CharField(max_length=100, blank=True, null=True)
	clastname = models.CharField(max_length=100, blank=True, null=True)
	date=models.DateField(auto_now_add=True, db_index=True, blank=True, null=True)
	total = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
	address1 = models.TextField(blank=True, null=True)
	address2 = models.TextField(blank=True, null=True)
	cp = models.IntegerField(blank=True, null=True)
	tel = models.IntegerField(blank=True, null=True)
	city = models.CharField(null=True, blank=True, max_length=100)
	country = models.CharField(blank=True, null=True, max_length=100)
	pagado = models.BooleanField(default=False)
	

	def __str__(self):
		return 'order {}'.format(self.id)

class Quantity(models.Model):
	order = models.ForeignKey(Order, related_name='item', blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	product = models.ForeignKey(Producto , blank=True, null=True)

	def __str__(self):
		return '{} shirt(s) id {} in order {}'.format(self.quantity, self.product.id, self.order.id)

