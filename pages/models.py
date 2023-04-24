from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    name = models.CharField(verbose_name="Название подкатегории", max_length=150, unique=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
