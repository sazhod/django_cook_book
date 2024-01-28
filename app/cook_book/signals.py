from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Recipe, ProductInRecipe, Product
from .utils import update_product_count_of_uses


@receiver(post_delete, sender=ProductInRecipe)
def delete_product_in_recipe(sender, instance, using, **kwargs):
    update_product_count_of_uses(instance)


@receiver(post_save, sender=ProductInRecipe)
def save_product_in_recipe(sender, instance, using, **kwargs):
    update_product_count_of_uses(instance)
