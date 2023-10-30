from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, г': 0.2,
    },
    'pasta': {
        'макароны, кг': 0.15,
        'сыр, кг': 0.03,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe):
    ingredients = {}
    servings = int(request.GET.get('servings', 1))
    if DATA.get(recipe):
        for k, v in DATA.get(recipe).items():
            ingredients[k] = v * servings
    context = {
        'recipe': ingredients,
        'head': recipe
    }
    res = render(request, 'calculator/index.html', context)
    return HttpResponse(res)
