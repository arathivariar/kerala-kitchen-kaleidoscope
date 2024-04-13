from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<description:description>/', views.recipe_detail, name='recipe_detail'),
]