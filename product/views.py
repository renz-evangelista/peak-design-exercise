from rest_framework import viewsets
from .models import Product, Store
from rest_framework.response import Response
from .serializers import ProductSerializer, StoreSerializer
from django.utils import timezone

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update_inventory(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)

        # Update the inventory_quantity and inventory_updated_time value
        new_inventory_quantity = request.data.get('inventory_quantity')
        product.inventory_quantity = new_inventory_quantity
        product.inventory_updated_time = timezone.now()
        product.save()

        # Return the updated product data
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
