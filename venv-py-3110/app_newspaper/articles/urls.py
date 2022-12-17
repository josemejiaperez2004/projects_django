#IMPORTACIONES
from django.urls import path
#IMPORTACION DE LA VIEW DE LOS ARTICLES
from .views import (
    ArticleListView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView,

)
"""
    Llamado de urls y sobre nombres para cada una para la navegacion
"""
urlpatterns = [


    path('', ArticleListView.as_view(), 
    name='article_list'
    ),

    path("<int:pk>/delete/", ArticleDeleteView.as_view(),
    name="article_delete"
    ),
    
    path("<int:pk>/", ArticleDetailView.as_view(),
    name="article_detail"
    ),

    path("<int:pk>/edit/", ArticleUpdateView.as_view(),
    name="article_edit"
    ),
        
    path("new/", ArticleCreateView.as_view(),
    name='article_new'
    ),

    



]