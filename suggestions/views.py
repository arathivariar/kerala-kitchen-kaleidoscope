from django.shortcuts import render
from django.contrib import messages
from .models import Suggestions
from .forms import SuggestionsForm


# Create your views here.
def suggestions(request):
    """
    Renders the suggestion form
    and allows user to submit suggestion requests.

    Displays an individual instance of :model:`suggestions.Suggestions`.

    **Context**
    ``suggestions``
        The most recent instance of :model:`suggestions.Suggestions`.
        ``suggestion_form``
            An instance of :form:`suggestions.SuggestionsForm`.

    **Template**
    :template:`suggestions/suggestions.html`
    """

    if request.method == "POST":
        suggestion_form = SuggestionsForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Suggestion received!'
            )
    suggestion = Suggestions.objects.all()
    suggestion_form = SuggestionsForm()

    return render(
        request,
        "suggestions/suggestions.html",
        {"suggestions": suggestions,
         "suggestion_form": suggestion_form},
    )