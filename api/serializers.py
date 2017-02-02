from rest_framework import serializers
from products.models import Producto, Color, Size

class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color 
		fields = ('color', 'id')

class SizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Size
		fields = ('quantity', 'size', 'id')

class ProductSerializer(serializers.ModelSerializer):
	color = ColorSerializer(many=True)
	stock = SizeSerializer(many=True)
	
	class Meta:
		model = Producto
		fields = ('name', 'image', 'color', 'price', 'stock', 'id')
		




