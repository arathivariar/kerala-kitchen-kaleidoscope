from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
@admin.site.register(Comment)


class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'dish_type')
    search_fields = ['title', 'ingredients']
    list_filter = ('dish_type','posted_on')
    prepopulated_fields = {'description': ('title',)}
    summernote_fields = ('method',)