#importaciones
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import CommentForm
from django.views.generic import(
    TemplateView,
    ListView,
    DetailView
)

# Create your views here.
#creacion de get para mostrar los comentarios enviados en el post
class CommentGet(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    #funcion de llamado de comentarios
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm() 
        return context


#creacion de post para enviar los comentarios a admin
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    #funcion para guarda el object 
    def post(self, request, *args, **kwargs):
        self.object = self.get_object ()
        return super().post(request, *args, **kwargs)
    #funcion para validar el formulario
    def form_valid(self, form):
        form.instance.author = self.request.user
        comment = form.save(commit = False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    #funcion de url
    def get_success_url(self):
        article = self.get_object ()
        return reverse("article_detail", kwargs={"pk": article.pk})
    #funcion que valida el autor del formulario
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

#Creacion de clase que traera los articulos  
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


#Clase que traera los comentarios y los mostrara
class ArticleDetailView(LoginRequiredMixin, DetailView):
    #muestra los comentarios
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    #Manda los cometnarios a la BD
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view ()
        return view(request, *args, **kwargs)
    


#Clase que actualiza los articulos solo si es el autor de ese
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    #Funcion para que solo el autor del articulo pueda modificarlo
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


#clase que elimina los articulos, solo si es el autor de ese        
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    
    #Funcion para que solo el autor del articulo pueda eliminarlo
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


#clase qeu crea un articulo desde 0, simepre y cuando este logueado
class ArticleCreateView (LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        
    )
    #funcion para que solo si esta logueado pueda crear el articulo
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#vista de error403
class Error403View(TemplateView):
    template_name = "errorScreens/error_403.html"


