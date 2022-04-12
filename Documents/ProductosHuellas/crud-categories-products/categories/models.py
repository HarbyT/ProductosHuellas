from django.db import models

# Create your models here.

class Category(models.Model):
    """ Categories for each product of the store """

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    sales = models.IntegerField(default=0)

    def get_products(self):
        return self.product_set.all()

    def __str__(self):
        return self.name
    