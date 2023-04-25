from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, StoreViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'store', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/inventory/', ProductViewSet.as_view({'post': 'update_inventory'}), name='product_update_inventory'),
]