from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

class CategoriesViews():
    """
    Parent generic view to avoid repeating
    the line indicating the view pattern.
    """

    model = models.Category

class CategoriesCUViews(CategoriesViews):
    """
    Parent generic view for the views responsible
    for creating and updating categories.
    """
    
    form_class = forms.CategoryForm
    success_url = reverse_lazy("categories:all")

# Create your views here.

class CategoryCreateView(CategoriesCUViews, generic.CreateView):
    template_name = "categories/create.html"

class CategoriesReadView(CategoriesViews, generic.ListView):
    template_name = "categories/read.html"
    context_object_name = "categories"

class CategoryUpdateView(CategoriesCUViews, generic.UpdateView):
    template_name = "categories/update.html"
    context_object_name = "category"

class CategoryDeleteView(CategoriesViews, generic.DeleteView):
    success_url = reverse_lazy("categories:all")

class CategoryDetailView(CategoriesViews, generic.DetailView):
    template_name = "categories/detail.html"
    context_object_name = "category"
