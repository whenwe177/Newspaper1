from django.contrib import admin
from .models import Article,Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    moodel = Comment

class ArticleAdmin(admin.ModelAdmin):
    inline = (
        CommentInline,
    )

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)