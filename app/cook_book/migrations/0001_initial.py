# Generated by Django 5.0.1 on 2024-01-27 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('count_of_uses', models.IntegerField(verbose_name='Кол-во использований')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_weight', models.IntegerField(verbose_name='Вес')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cook_book.product')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('products', models.ManyToManyField(through='cook_book.ProductInRecipe', to='cook_book.product')),
            ],
        ),
        migrations.AddField(
            model_name='productinrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cook_book.recipe'),
        ),
        migrations.AddConstraint(
            model_name='productinrecipe',
            constraint=models.UniqueConstraint(fields=('recipe', 'product'), name='unique_product_in_recipe'),
        ),
    ]
