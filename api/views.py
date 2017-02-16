from django.shortcuts import render
from rest_framework import viewsets
from products.models import Producto
from orders.models import Order
from api.serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
#
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
	
	queryset = Producto.objects.all()
	serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer


    	





