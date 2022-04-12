from django.contrib import admin

from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
        Admin View for Product
    """
    list_display = ('name', 'price', 'sales')
    list_filter = ('pub_date',)
    search_fields = ('name',)

admin.site.register(models.Product, ProductAdmin)
