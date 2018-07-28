from django.contrib import admin
from .models import Article, Tag, Entry


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'tagged', 'edited', 'created', 'article')
