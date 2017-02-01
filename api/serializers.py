from rest_framework import serializers
from products.models import Producto

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('name', 'image', 'size', 'color', 'price', 'stock', 'id')
