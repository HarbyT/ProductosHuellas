from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

class ProductsViews():
    """
    Parent generic view to avoid repeating
    the line indicating the view pattern.
    """

    model = models.Product

class ProductsCUViews(ProductsViews):
    """
    Parent generic view for the views responsible
    for creating and updating products.
    """

    form_class = forms.ProductForm
    success_url = reverse_lazy("products:all")

# Create your views here.

class ProductCreateView(ProductsCUViews, generic.CreateView):
    template_name = "products/create.html"

class ProductsReadView(ProductsViews, generic.ListView):
    template_name = "products/read.html"
    context_object_name = "products"

class ProductUpdateView(ProductsCUViews, generic.UpdateView):
    template_name = "products/update.html"
    context_object_name = "product"

class ProductDeleteView(ProductsViews, generic.DeleteView):
    success_url = reverse_lazy("products:all")

class ProductDetailView(ProductsViews, generic.DetailView):
    template_name = "products/detail.html"
    context_object_name = "product"

def counter_sales_view(request):
    product = get_object_or_404(models.Product, pk=request.POST['id_product'])

    if 'action' not in request.POST:
        context = {'product': product}
        return render(request, 'products/counter_sales.html', context)

    product.counter_sales()

    return HttpResponseRedirect(reverse('products:all'))

