from django.test import TestCase, Client
from django.urls import reverse

from categories import models

class CategoriesTestView(TestCase):
    """
    Check that the views of the categories app work 
    correctly and that they are well structured.
    """

    def setUp(self):
        self.client = Client()
        self.category = models.Category.objects.create(
            name="Electronics",
            description="The life is life"
        )

    def test_create_view(self):
        response = self.client.get(reverse('categories:create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/create.html')

    def test_read_view(self):
        response = self.client.get(reverse('categories:all'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/read.html')
        self.assertContains(response, self.category.name)

    def test_update_view(self):
        response = self.client.get(reverse('categories:update', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/update.html')
        self.assertContains(response, self.category.name)

    def test_delete_view(self):
        response = self.client.get(reverse('categories:delete', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'categories/category_confirm_delete.html'
        )

    def test_detail_view(self):
        response = self.client.get(reverse('categories:detail', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories/detail.html')
        self.assertContains(response, self.category.name)
