from django.test import TestCase, Client
from django.urls import reverse

class CommonTestViews(TestCase):
    """
    Check that the views of the products app work 
    correctly and that they are well structured.
    """

    def test_home_view(self):
        response = self.client.get(reverse('common:home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home.html')
        self.assertContains(response, 'Home')
