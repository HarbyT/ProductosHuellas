from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from categories import models as models_categories
from products import models as models_products

# Create your views here.

def home_view(request):
    return render(request, 'common/home.html')
