#Importaciones
from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInLine (admin.StackedInline):
    model = Comment
    Extra = 0

class ArticleAdmin (admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

#Administrador de vistas
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)