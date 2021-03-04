from django.contrib import admin

from .models import *


class News_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("author",)}


admin.site.register(News_post, News_postAdmin)
admin.site.register(Comment, CommentAdmin)

