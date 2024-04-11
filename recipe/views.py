from django.shortcuts import render
from django.views import generic
from .models import Recipe

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipe/index.html"
    paginate_by = 6