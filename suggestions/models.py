from django.db import models


# Create your models here.


class Suggestions(models.Model):
    """
    Stores a suggestion
    """

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.title


class SuggestionRequest(models.Model):
    """
    Stores a single suggestion request message
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
