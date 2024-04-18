from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

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


@login_required
def comment_edit(request, recipe_id, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.
    ``comment``
        A single comment related to the recipe.
    ``comment_form``
        An instance of :form:`recipe.CommentForm`
    """
    if request.method == "POST":

        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, recipe_id=recipe_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("recipe_detail", args=[recipe_id]))


@login_required
def comment_delete(request, recipe_id, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Recipe`.
    ``comment``
        A single comment related to the recipe.
    """
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, recipe_id=recipe_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[recipe_id]))
