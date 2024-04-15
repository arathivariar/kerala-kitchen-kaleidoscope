from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Recipe, Comment
from .forms import CommentForm

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipe/index.html"
    paginate_by = 6


def recipe_detail(request, recipe_id):
    """
    Display an individual :model:`recipe.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.

    **Template:**

    :template:`recipe/recipe_detail.html`
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, recipe_id=recipe_id)
    comments = recipe.comments.all().order_by("-posted_on")
    comment_count = recipe.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,'Comment submitted and awaiting approval')
        comment_form = CommentForm()

    return render(
        request,
        "recipe/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )