from rest_framework import serializers
from ..models import Order, Quantity
from products.models import Producto

class QuantitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Quantity
		fields = ('quantity','product')



class OrderSerializer(serializers.ModelSerializer):
	item = QuantitySerializer(many=True)	
	class Meta:
		model = Order
		fields = ('id', 'cname', 'clastname','total', 'address1', 'address2', 'cp', 'tel', 'city', 'country', 'item' )
	


	def create(self, validated_data):
		
		order_data = validated_data.pop('item')
		order = Order.objects.create(**validated_data)
		
		
		for o in order_data:
			p = o['product']
			
			q = o['quantity']
			
			Quantity.objects.create(order=order,quantity=q, product=p)
		return order

#'item': [OrderedDict([('quantity', 2), ('product', <Producto: playeron>)])],


	
