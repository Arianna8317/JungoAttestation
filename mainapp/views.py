# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import RecipeSearchForm
# from .forms import ProductForm, ImageForm


# Create your views here.

def about(request):
    return HttpResponse("Сайт создан в качестве итогового проекта по Django")


def index(request):
    random_5 = Recipe.objects.order_by('?')[:5]
    return render(request, 'mainapp/index.html',  {'recipes': random_5})


def recipe_search(request):
    if request.method == 'POST':
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data['name']
            
            recipe = get_object_or_404(Recipe, name=recipe_name)
            #recipe = Recipe.objects.filter(name = recipe_name).values()[:1]
            return render(request, 'mainapp/full_recipe_show.html', {'recipe': recipe})  
    else:
        form = RecipeSearchForm()
        return render(request, 'mainapp/recipe_search.html', {'form':  form}) 
    

    