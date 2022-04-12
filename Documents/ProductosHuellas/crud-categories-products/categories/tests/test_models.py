from django.test import TestCase

from categories.models import Category

class CategoryTestModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics", 
            description="Lorem Ipsum",
            sales=3
        )

    def test_creating_category(self):
        """ checks category creation """

        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Lorem Ipsum")
        self.assertEqual(self.category.sales, 3)
