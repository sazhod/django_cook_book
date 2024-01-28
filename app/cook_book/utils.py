from django.db.models import Count, QuerySet
from .models import ProductInRecipe, Product


def update_product_count_of_uses(instance):
    count_of_uses = ProductInRecipe.objects.filter(product=instance.product).count()
    product = Product.objects.get(pk=instance.product.pk)
    product.count_of_uses = count_of_uses
    product.save()


def update_or_create_product_in_recipe(recipe_id: int, product_id: int, weight: int):
    """
    Функция отвечающая за обновление веса продукта(если такой продукт уже существует в рецепте) или добавление
        нового в рецепт.
    """
    default_data = {
        'product_weight': weight
    }
    ProductInRecipe.objects.update_or_create(recipe_id=recipe_id, product_id=product_id, defaults=default_data)


def update_product_count_of_uses_in_recipe(recipe_id: int):
    """
    Функция отвечающая за обновление количества использования всех продуктов связанных с рецептом.
    """
    for productInRecipe in ProductInRecipe.objects.filter(recipe_id=recipe_id).select_related():
        Product.objects.filter(pk=productInRecipe.product.pk).update(
            count_of_uses=productInRecipe.product.count_of_uses + 1)


def get_recipes_without_product(product_id: int) -> QuerySet:
    """
    Функция отвечающая за получение рецептов в которых нет указанного продукта, либо его содержание меньше 10грамм.
    """
    excluded_productInRecipe = ProductInRecipe.objects.filter(product_id=product_id, product_weight__gte=10).values(
        'recipe_id')
    recipes = (ProductInRecipe.objects.filter(
        product_id=product_id,
        product_weight__lt=10
    ) ^ ProductInRecipe.objects.exclude(
        recipe_id__in=excluded_productInRecipe
    )).select_related().values(
        'recipe__id',
        'recipe__title'
    ).annotate(count=Count('recipe__id'))

    return recipes
