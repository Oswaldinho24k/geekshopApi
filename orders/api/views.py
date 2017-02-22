from django.shortcuts import render
from rest_framework import viewsets
from ..models import Order, Quantity
from .serializers import OrderSerializer
from rest_framework.response import Response

from django.http import HttpResponse
from rest_framework.decorators import detail_route


class OrderViewSet(viewsets.ModelViewSet):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@detail_route(methods=['get'], serializer_class=OrderSerializer)
	def orders(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@detail_route(methods=['post'])
	def item(self, request, *args, **kwargs):
		order = self.get_object()
		order.item.add(quantity, order, product)
		return HttpResponse({'enrolled':True})
