from django.test import TestCase

from categories import forms

class CategoriesTestForms(TestCase):

    def test_category_form_valid_data(self):
        form = forms.CategoryForm(data={
            'name': 'Electronics',
            'description': 'Hey, Hi, Hello!'
        })

        self.assertTrue(form.is_valid())

    def test_category_form_no_data(self):
        form = forms.CategoryForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
