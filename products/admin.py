from django.contrib import admin
from .models import Producto, Size, Color, Imagini

# Register your models here.
admin.site.register(Producto)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Imagini)