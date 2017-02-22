from rest_framework import serializers
from ..models import Order, Quantity

class QuantitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Quantity
		fields = ('quantity','product')

class OrderSerializer(serializers.ModelSerializer):
	item = QuantitySerializer(many=True)
	class Meta:
		model = Order
		fields = ('id', 'cname', 'clastname','total', 'address1', 'address2', 'cp', 'tel', 'city', 'country', 'item' )

