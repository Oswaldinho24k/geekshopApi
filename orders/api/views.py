from django.shortcuts import render
from rest_framework import viewsets
from ..models import Order, Quantity
from .serializers import OrderSerializer
from rest_framework.response import Response
#
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def item_create(self, serializer):
		serializer.save(item=self.request.data['item'])
	def item_update(self, serializer):
		serializer.save(item=self.request.data['item'])
