from django import forms
import datetime
from .models import Recipe

from django import forms
import datetime
class ImageForm(forms.Form):
    image = forms.ImageField()

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    image = forms.ImageField()

class RecipeSearchForm(forms.Form):
    name = forms.CharField(max_length=50)



class CategorySelect(forms.Select):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
   
        return option


class RecipeForm1(forms.ModelForm):
    class Meta:
        model = Recipe 
        fields = ["category"]
        widgets = {"category": CategorySelect} 


        
