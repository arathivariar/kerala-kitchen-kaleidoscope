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
            An instance of :form:`suggestions.SuggestionForm`.

    **Template**
    :template:`suggestions/suggestions.html`
    """

    if request.method == "POST":
        suggestion_form = SuggestionForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Suggestion request received!'
            )
    suggestion = Suggestions.objects.all()
    suggestion_form = SuggestionForm()

    return render(
        request,
        "suggestions/suggestions.html",
        {"suggestions": suggestions,
         "suggestion_form": suggestion_form},
    )