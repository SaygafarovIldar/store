from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug", "category")
    list_display_links = ("pk", "name")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "product_type", "category")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category",)
    inlines = [ProductImageInline]