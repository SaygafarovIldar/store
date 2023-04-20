from django.urls import path
from . import views

app_name = "main"
# {% url 'main:home' %}
urlpatterns = [
    path("", views.home_view, name="home"),
    path("categories/", views.shop_view, name="shop"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail")
]