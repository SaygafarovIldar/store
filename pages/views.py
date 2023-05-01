from django.shortcuts import render, HttpResponse
from .models import Product, Subcategory

# Create your views here.


def home_view(request):
    return render(request, "pages/index.html")


def shop_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def subcategory_products_view(request, slug):
    subcategory = Subcategory.objects.get(slug=slug)
    products = Product.objects.filter(subcategory=subcategory)
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def product_detail(request, slug):
    return render(request, "pages/product_detail.html")