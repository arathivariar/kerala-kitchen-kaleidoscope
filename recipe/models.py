from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    description = models.SlugField(max_length=200, unique=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kitchen_recipes")
    ingredients = models.TextField()
    method = models.TextField()
    dish_type = models.CharField(max_length=200)
    prep_time = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)