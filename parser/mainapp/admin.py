from django.contrib import admin
from .models import Author, Hab, Article


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Hab)
class HabModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    pass
