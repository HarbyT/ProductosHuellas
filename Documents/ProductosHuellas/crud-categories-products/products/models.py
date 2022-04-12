import datetime

from django.db import models
from django.utils import timezone

from categories.models import Category

# Create your models here.

class Product(models.Model):
    """ Porducts of the store """

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    pub_date = models.DateField(default=timezone.now)
    sales = models.IntegerField(default=0)
    available = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def counter_sales(self):
        self.sales += 1
        category = self.category
        category.sales += 1 
        category.save()
        self.available -= 1
        
        if self.available <= 0:
            is_available = False

        self.save()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.name
    