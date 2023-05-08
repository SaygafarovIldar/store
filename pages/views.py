from django.shortcuts import render, HttpResponse
from .models import Product, Subcategory
from django.core.paginator import Paginator

# Create your views here.


def home_view(request):
    return render(request, "pages/index.html")


def shop_view(request):
    products = Product.objects.all()
    paginator = Paginator(products, 1)
    page = request.GET.get("page")
    result = paginator.get_page(page)

    context = {
        "products": result
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
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category)
    context = {
        "product_detail": product,
        "related_products": related_products
    }
    return render(request, "pages/product_detail.html", context)