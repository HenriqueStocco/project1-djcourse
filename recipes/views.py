from django.shortcuts import render
from utils.recipes.factory_recipes import make_recipe
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    '''
    Em filter, queros pegar os IDs das categorias, para acessar esses ids
    fica category__id(um campo de Recipe que esta relacionado com Category)=category_id(que e o nome que a url informa)
    '''
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
