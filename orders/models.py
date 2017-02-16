from django.db import models
from django.contrib.auth.models import User
from products.models import Producto


# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(User)
    date = models.DateTimeField(auto_now=True, db_index=True)
    products = models.ForeignKey(Producto)
    total = models.DecimalField(decimal_places=2, max_digits=5)
    address = models.TextField()

    def __str__(self):
        return self.id
