from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
  
    def __str__(self):
        return f'Категория рецептов: {self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.TextField()
    steps = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to=None)
    time = models.PositiveIntegerField()

    def __str__(self):
        return f'Название: {self.name}.   Описание: {self.description}  {self.category}'





