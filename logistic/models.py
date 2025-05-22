from django.db import models

class Visit(models.Model):
    ip_address = models.GenericIPAddressField()
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ip_address} - {self.city}, {self.country} at {self.timestamp}"
