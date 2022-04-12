from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "common"
urlpatterns = [
    # ex: /
    path("", views.home_view, name="home"),
]