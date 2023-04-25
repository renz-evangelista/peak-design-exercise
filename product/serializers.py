from rest_framework import serializers
from .models import Product, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'url']
        read_only_fields = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    store_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'inventory_quantity', 'inventory_updated_time', 'store_id']

    def create(self, validated_data):
        store_id = validated_data.pop('store_id')
        product = Product.objects.create(store_id=store_id, **validated_data)
        return product
        