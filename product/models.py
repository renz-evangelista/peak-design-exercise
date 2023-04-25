from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    inventory_quantity = models.PositiveIntegerField(default=0)
    inventory_updated_time = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
