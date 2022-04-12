from django.test import TestCase
from django.urls import resolve, reverse

from products import views

class ProductsTestUrls(TestCase):
    """
    Check that the urls of the products app work 
    correctly and that they are well structured.
    """

    def test_create_url_resolves(self):
        url = reverse('products:create')
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProductCreateView
        )

    def test_read_url_resolves(self):
        url = reverse('products:all')
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProductsReadView
        )

    def test_update_url_resolves(self):
        url = reverse('products:update', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProductUpdateView
        )

    def test_delete_url_resolves(self):
        url = reverse('products:delete', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProductDeleteView
        )

    def test_detail_url_resolves(self):
        url = reverse('products:detail', args=['1'])
        self.assertEquals(
            resolve(url).func.view_class,
            views.ProductDetailView
        )

    def test_counter_sales_url_resolves(self):
        url = reverse('products:counter_sales')
        self.assertEquals(
            resolve(url).func,
            views.counter_sales_view
        )
