from django import template
from pages.models import Category, Subcategory

register = template.Library()
# [("cat 1", ("subcat 1", "subcat 2"))]
"""
categories = {
    "cat1": ["subcat 1", "subcat 2"],
    "cat2": ["subcat 1", "subcat 2"],
}
"""


@register.simple_tag()
def get_categories_data():
    categories = Category.objects.all()
    data = {category: category.categories.all() for category in categories}
    return data
