from django.db import models
from django.contrib.auth.models import User
from products.models import Producto


# Create your models here.
class Quantity(models.Model):
    quantity = models.IntegerField()
    product = models.OneToOneField(Producto)

    def __str__(self):
        return '{} of {}'.format(self.quantity, self.product.name)


class Order(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    cname = models.CharField(max_length=100, blank=True, null=True)
    clastname = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True, db_index=True, blank=True, null=True)
    # products=models.ManyToManyField(Producto, blank=True)
    quantity = models.ManyToManyField(Quantity, related_name='q', blank=True, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=100, blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    city = models.CharField(null=True, blank=True, max_length=100)
    country = models.CharField(blank=True, null=True, max_length=100)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.cname
