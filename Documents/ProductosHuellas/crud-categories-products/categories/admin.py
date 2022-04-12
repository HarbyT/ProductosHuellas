from django.contrib import admin

from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """ 
        Admin View for Categories
    """
    list_display = ('name', 'sales')
    list_filter = ('sales',)
    search_fields = ('name',)

admin.site.register(models.Category, CategoryAdmin)
    