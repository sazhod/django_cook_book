from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404
from django.utils.datastructures import MultiValueDictKeyError
from .models import ProductInRecipe, Product, Recipe
from .utils import (update_or_create_product_in_recipe,
                    update_product_count_of_uses_in_recipe,
                    get_recipes_without_product)


def index(request):
    return render(request, 'cook_book/index.html')


def add_product_to_recipe(request):
    try:
        recipe_id = int(request.GET['recipe_id'])
        product_id = int(request.GET['product_id'])
        weight = int(request.GET['weight'])
    except MultiValueDictKeyError:
        raise Http404('Убедитесь что были переданы все необходимые параметры.')
    except ValueError:
        raise Http404('Убедитесь переданные параметры имеют верное значение.')

    update_or_create_product_in_recipe(recipe_id, product_id, weight)

    return redirect(index)


def cook_recipe(request):
    try:
        recipe_id = int(request.GET['recipe_id'])
    except MultiValueDictKeyError:
        raise Http404('Убедитесь что были переданы все необходимые параметры.')
    except ValueError:
        raise Http404('Убедитесь переданные параметры имеют верное значение.')

    update_product_count_of_uses_in_recipe(recipe_id)

    return redirect(index)


def show_recipes_without_product(request):
    try:
        product_id = int(request.GET['product_id'])
    except MultiValueDictKeyError:
        raise Http404('Убедитесь что были переданы все необходимые параметры.')
    except ValueError:
        raise Http404('Убедитесь переданные параметры имеют верное значение.')

    data = {
        'recipes': get_recipes_without_product(product_id)
    }

    return render(request, 'cook_book/index.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена. {exception}')
