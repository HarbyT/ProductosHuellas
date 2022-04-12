from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    # ex: /products/create/
    path(
        "create/",
        views.ProductCreateView.as_view(),
        name="create"
    ),
    # ex: /products/all/
    path(
        "all/",
        views.ProductsReadView.as_view(),
        name="all"
    ),
    # ex: /products/update/12
    path(
        "update/<int:pk>",
        views.ProductUpdateView.as_view(),
        name="update"
    ),
    # ex: /products/delete/12
    path(
        "delete/<int:pk>",
        views.ProductDeleteView.as_view(),
        name="delete"
    ),
    # ex: /products/datail/12
    path(
        "detail/<int:pk>",
        views.ProductDetailView.as_view(),
        name="detail"
    ),
    # ex: /products/counter_sales/
    path(
        "counter_sales/",
        views.counter_sales_view,
        name="counter_sales"
    ),
]
