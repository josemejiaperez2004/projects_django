#IMPORTACIONES
from django import forms
from .models import Comment

#Clase de comentarios, Author + cuerpo del comentario
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
