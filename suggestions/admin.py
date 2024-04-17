from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Suggestions, SuggestionRequest


@admin.register(Suggestions)
class Suggestions(SummernoteModelAdmin):
    """
    Adds rich-text editing of message in admin
    """
    summernote_fields = ('message',)


@admin.register(SuggestionRequest)
class SuggestionRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)