from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('recipe_id', 'title', 'description', 'dish_type')
    search_fields = ['title', 'ingredients']
    list_filter = ('dish_type','posted_on',)
    prepopulated_fields = {'description': ('title',)}
    summernote_fields = ('method',)

# Register your models here.
admin.site.register(Comment)