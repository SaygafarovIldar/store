from django.contrib import admin
from .models import Category, Subcategory

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