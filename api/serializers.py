from rest_framework import serializers
from products.models import Producto


class ProductSerializer(serializers.ModelSerializer):
	stock = serializers.StringRelatedField(many=True)
	color = serializers.StringRelatedField(many=True)

	
	class Meta:
		model = Producto
		fields = ('name', 'image', 'color', 'price', 'stock', 'id')
		




