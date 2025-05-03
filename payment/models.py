from django.db import models

# Create your models here.
class paydata(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    iscomplete = models.BooleanField(default=False)
    stirpe_session_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_link_id = models.CharField(max_length=255, blank=True, null=True)


class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    productlist = models.Charfield(max_length=512)