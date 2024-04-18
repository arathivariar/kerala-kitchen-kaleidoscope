from django import forms
from .models import Suggestions


class SuggestionsForm(forms.ModelForm):
    """
    Form class for users to submit a suggestion
    """

    class Meta:
        """
        Specify the django model and order of the fields
        """

        model = Suggestions
        fields = ("name", "email", "message")
