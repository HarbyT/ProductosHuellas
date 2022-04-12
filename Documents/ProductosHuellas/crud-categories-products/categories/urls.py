from django.urls import path

from . import views

app_name = "categories"

urlpatterns = [
    # ex: /categories/create/
    path(
        "create/",
        views.CategoryCreateView.as_view(),
        name="create"
    ),
    # ex: /categories/all/
    path(
        "all/",
        views.CategoriesReadView.as_view(),
        name="all"
    ),
    # ex: /categories/update/13
    path(
        "update/<int:pk>",
        views.CategoryUpdateView.as_view(),
        name="update"
    ),
    # ex: /categories/delete/13
    path(
        "delete/<int:pk>",
        views.CategoryDeleteView.as_view(),
        name="delete"
    ),
    # ex: /categories/detail/12
    path(
        "detail/<int:pk>",
        views.CategoryDetailView.as_view(),
        name="detail"
    )
]
