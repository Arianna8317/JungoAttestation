# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import RecipeSearchForm
from . import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def about(request):
    return render(request, 'mainapp/about.html')


def index(request):
    random_5 = Recipe.objects.order_by('?')[:5]
    return render(request, 'mainapp/index.html',  {'recipes': random_5})

def home(request):
    recipes = models.Recipe.objects.all()
    
    return render(request, 'mainapp/home.html', {'recipes': recipes})

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
    


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')


def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['name', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    