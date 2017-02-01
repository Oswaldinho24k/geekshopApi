from rest_framework import serializers
from products.models import Producto

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'imagen', 'talla', 'color', 'precio', 'stock', 'id')
