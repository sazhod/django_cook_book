from django.contrib import admin
from .models import Product, Recipe, ProductInRecipe


class ProductInRecipeInline(admin.TabularInline):
    model = ProductInRecipe
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ProductInRecipeInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['count_of_uses']
    list_display = ['id', 'title', 'count_of_uses']
