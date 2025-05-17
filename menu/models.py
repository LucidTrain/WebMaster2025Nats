from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    preparation_process = models.TextField(max_length=1000, blank=True)
    farm_name = models.CharField(max_length=255, blank=True)
    farm_address = models.CharField(max_length=255, blank=True)


    
