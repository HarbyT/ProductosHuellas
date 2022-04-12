from django.test import TestCase
from django.urls import resolve, reverse

from categories import views

class CategoriesTestUrls(TestCase):
    """
    Check that the urls of the categories app work 
    correctly and that they are well structured.
    """

    def test_create_url_resolves(self):
        url = reverse('categories:create')
        self.assertEquals(
            resolve(url).func.view_class,
            views.CategoryCreateView
        )

    def test_read_url_resolves(self):
        url = reverse('categories:all')
        self.assertEquals(
            resolve(url).func.view_class,
            views.CategoriesReadView
        )

    def test_update_url_resolves(self):
        url = reverse('categories:update', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.CategoryUpdateView
        )

    def test_delete_url_resolves(self):
        url = reverse('categories:delete', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.CategoryDeleteView
        )

    def test_detail_url_resolves(self):
        url = reverse('categories:detail', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.CategoryDetailView
        )
