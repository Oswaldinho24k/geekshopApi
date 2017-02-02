from django.shortcuts import render
from rest_framework import viewsets
from products.models import Producto
from api.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer





