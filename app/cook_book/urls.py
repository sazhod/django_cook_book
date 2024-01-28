from django.contrib import admin
from django.urls import path, include
from .views import index, add_product_to_recipe, show_recipes_without_product, cook_recipe


urlpatterns = [
    path('', index),
    path(r'add_product_to_recipe/', add_product_to_recipe),
    path('show_recipes_without_product/', show_recipes_without_product),
    path('cook_recipe/', cook_recipe),
]
