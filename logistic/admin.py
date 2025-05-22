from django.contrib import admin
from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ( 'timestamp','city', 'country', 'ip_address')
    list_filter = ('city', 'timestamp')

admin.site.register(Visit, VisitAdmin)
# Register your models here.
