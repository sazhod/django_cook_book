from django.db import models


class Product(models.Model):
    """
    Модель описывающая Продукт.
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    count_of_uses = models.IntegerField(verbose_name='Кол-во использований', default=0, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """
    Модель описывающая рецепт. Имеет связь многие ко многим с моделью Product.
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    products = models.ManyToManyField(Product, through='ProductInRecipe')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class ProductInRecipe(models.Model):
    """
    Модель описывающая продукты и рецепты. Необходима для хранения дополнительных данных в связи многие ко многим,
        а также для реализации дополнительной логики.
    Ограничение реализованное в constraints необходимо для добавления уникальных продуктов в рецепт при работе через
        админ панель.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='products')
    product_weight = models.IntegerField(verbose_name='Вес (грамм)')

    class Meta:
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецепте'
        constraints = [
            models.UniqueConstraint(
                fields=("recipe", "product"), name="unique_product_in_recipe"
            ),
        ]

    def __str__(self):
        return f'{self.recipe}_{self.product}'

