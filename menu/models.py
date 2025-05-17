from django.db import models
import stripe
# Create your models here.
from django.conf import settings

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True)
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True, editable=False)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True, editable=False)
    preparation_process = models.TextField(max_length=1000, blank=True)
    farm_name = models.CharField(max_length=255, blank=True)
    farm_address = models.CharField(max_length=255, blank=True)
    description =  models.CharField(max_length=255, blank=True)
    def save(self, *args, **kwargs):
        if not self.stripe_product_id:
            stripe.api_key = settings.STRIPE_API
            product = stripe.Product.create(
                name = self.title, 
                description=self.description or "00",)
            self.stripe_product_id = product.id
        price = stripe.Price.create(
            unit_amount=int(self.price * 100),
            currency="usd",
            product=self.stripe_product_id,
            )
        self.stripe_price_id = price.id
        super().save(*args, **kwargs)
    
