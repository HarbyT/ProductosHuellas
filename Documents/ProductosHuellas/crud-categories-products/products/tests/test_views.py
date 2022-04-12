from django.test import TestCase, Client
from django.urls import reverse

from categories import models as models_categories
from products import models as models_products

class ProductsTestView(TestCase):
    """
    Check that the views of the products app work 
    correctly and that they are well structured.
    """

    def setUp(self):
        self.client = Client()
        self.category = models_categories.Category.objects.create(
            name="Electronics",
            description="The life is life"
        )
        self.product = models_products.Product.objects.create(
            name="Computer DX10",
            description="The life is life",
            price=10,
            available=20,
            category=self.category
        )

    def test_create_view(self):
        response = self.client.get(reverse('products:create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create.html')

    def test_read_view(self):
        response = self.client.get(reverse('products:all'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/read.html')
        self.assertContains(response, self.product.name)

    def test_update_view(self):
        response = self.client.get(reverse('products:update', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update.html')
        self.assertContains(response, self.product.name)

    def test_delete_view(self):
        response = self.client.get(reverse('products:delete', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'products/product_confirm_delete.html'
        )

    def test_detail_view(self):
        response = self.client.get(reverse('products:detail', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/detail.html')
        self.assertContains(response, self.product.name)

    def test_counter_sales_view(self):
        response = self.client.post(reverse('products:counter_sales'), {
            'id_product': 1
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/counter_sales.html')
        self.assertContains(response, 'register')
