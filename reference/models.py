from django.db import models

# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=200, blank=True)
    link = models.TextField(blank=True)
