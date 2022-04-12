from django.test import TestCase

from categories import models
from products import forms 

class ProductsTestForms(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(
            name='Electronics',
            description='Hey, Hi, Hello!'
        )

    def test_product_form_valid_data(self):
        form = forms.ProductForm(data={
            'name': 'Computer DX10',
            'description': 'Hey, Hi, Hello!',
            'price': 50,
            'available': 10,
            'category': self.category
        })

        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = forms.ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
