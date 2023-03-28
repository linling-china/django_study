from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_titles, name='blog_titles'),
    path('<int:article_id>/', views.blog_arctile, name='blog_article')
]