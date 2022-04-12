from django.test import TestCase
from django.utils import timezone

from categories.models import Category
from products.models import Product

class ProductTestModel(TestCase):
    def setUp(self):
        self.datetime = timezone.now()
        self.category = Category.objects.create(
            name="Electronics", 
            description="Lorem Ipsum",
        )
        self.product = Product.objects.create(
            name="Computer DX10 V2",
            description="Lorem Ipsum",
            price=21,
            pub_date=self.datetime,
            available=20,
            category=self.category,
        )

    def test_creating_product(self):
        """ check product creation """

        self.assertEqual(self.product.name, "Computer DX10 V2")
        self.assertEqual(self.product.description, "Lorem Ipsum")
        self.assertEqual(self.product.price, 21)
        self.assertEqual(self.product.pub_date, self.datetime)
        self.assertEqual(self.product.sales, 0)
        self.assertEqual(self.product.available, 20)
        self.assertEqual(self.product.is_available, True)

    def test_counter_sales(self):
        """ 
        verifies the corret operation of
        the sales counter of each product
        """

        self.product.counter_sales()

        self.assertEqual(self.product.sales, 1)
        self.assertEqual(self.product.available, 19)
        self.assertEqual(self.category.sales, 1)

    def test_was_published_recently(self):
        """
        check if the product has been
        published recently
        """

        self.assertEqual(self.product.was_published_recently(), True)
