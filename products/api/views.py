from django.shortcuts import render
from rest_framework import viewsets
from ..models import Producto
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
	
	queryset = Producto.objects.all()
	serializer_class = ProductSerializer


