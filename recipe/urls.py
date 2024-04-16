from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/edit_comment/<int:comment_id>', 
        views.comment_edit, name='comment_edit'),
    path('<int:recipe_id>/delete_comment/<int:comment_id>', 
        views.comment_delete, name='comment_delete'),
]