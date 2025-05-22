from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

admin.site.register(Listing, ListingAdmin)

# Register your models here.
