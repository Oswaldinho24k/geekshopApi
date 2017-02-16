from rest_framework import serializers
from products.models import Producto, Color, Size, Imagini
from orders.models import Order,  Quantity

class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color 
		fields = ('name', 'hexa')

class SizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Size
		fields = ('quantity', 'size', 'id')

class ImaginiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Imagini
		fields = ('img', 'prod')

class ProductSerializer(serializers.ModelSerializer):
	colors = ColorSerializer(many=True)
	stock = SizeSerializer(many=True)
	producto = ImaginiSerializer(many=True)

	class Meta:
		model = Producto
		fields = ('name', 'colors', 'price', 'stock', 'id', 'producto')

class QuantitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Quantity
		fields = ('quantity', 'product', 'order')


class OrderSerializer(serializers.ModelSerializer):
	
	quantity = serializers.StringRelatedField(many=True)
	class Meta:
		model = Order
		fields = ('id','quantity', 'cname', 'clastname', 'address1', 'address2','cp', 'tel', 'date', 'total', 'country', 'city')
		





