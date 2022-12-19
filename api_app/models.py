from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=7, max_length=10, decimal_places=2)
    stock=models.CharField(max_length=100)
    discount_price=models.DecimalField(max_digits=7, decimal_places=2)
    category=models.CharField(max_length=100, null=True, blank=True )

    def __str__(self):
        return self.name
