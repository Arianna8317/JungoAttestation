from django.contrib import admin

# Register your models here.
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description']
    ordering = ['name']   
    search_fields = ['name']
    search_help_text = 'Поиск по полю Название рецепта' 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)