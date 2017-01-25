from django.shortcuts import render
from django.views.generic import View
from .models import Producto

# Create your views here.

class losProductos(View):

	def get(self, request):
		productos = Producto.objects.all()
		template_name = 'productos.html'

		context = {
			'productos':productos
		}

		return render (request, template_name, context)