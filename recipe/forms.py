from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a recipe
    """
    class Meta:
        """
        Specify the Django model and order of the fields
        """
        model = Comment
        fields = ('body',)