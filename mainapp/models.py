from django.db import models
from django.contrib.auth.models import User
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to=None)
    time = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'Название: {self.name}.   Описание: {self.description}  {self.category}'





