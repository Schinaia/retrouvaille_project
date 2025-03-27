from django.urls import path
from . import views

from .views import ArticleListView, AuthorDetailview


urlpatterns =[
     path("", ArticleListView.as_view(),name="article-list"),
     path("author/<int:pk>/", AuthorDetailview.as_view(),name="author-detail"), 
     path('create/', views.create_article, name='create_article'),
     path('articles/', views.article_list, name='article_list'),
     
]
