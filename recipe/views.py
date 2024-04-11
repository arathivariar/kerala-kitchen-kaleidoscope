from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipe/index.html"
    paginate_by = 6


    def recipe_detail(request, description):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(dish_type="curries")
    recipe = get_object_or_404(queryset, description=description)

    return render(
        request,
        "recipe/recipe_detail.html",
        {"recipe": recipe},
    )