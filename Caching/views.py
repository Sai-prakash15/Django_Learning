from django.shortcuts import render
from .models import Recipe

from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_recipes():
    # Queries 3 tables: cookbook_recipe, cookbook_ingredient,
    # and cookbook_food.
    # print(Recipe.objects.prefetch_related('ingredient_set__food'))
    return list(Recipe.objects.prefetch_related('ingredient_set__food'))

@cache_page(CACHE_TTL)
def recipes_view(request):
    return render(request, 'recipes.html', {
        'recipes': get_recipes()
    })