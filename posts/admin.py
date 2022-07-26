from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Article, ArticleAdmin)
