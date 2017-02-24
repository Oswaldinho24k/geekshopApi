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

	def create(self, validated_data):
		return Quantity.objects.create(**validated_data)