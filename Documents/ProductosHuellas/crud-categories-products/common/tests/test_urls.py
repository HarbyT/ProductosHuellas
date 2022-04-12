from django.test import TestCase
from django.urls import resolve, reverse

from common import views

class CommonTestUrls(TestCase):
    """
    Check that the urls of the products app work 
    correctly and that they are well structured.
    """

    def test_home_url_resolves(self):
        url = reverse('common:home')

        self.assertEquals(resolve(url).func, views.home_view)
