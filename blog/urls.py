from django.urls import path
from . import views

# Namespace for blog URLs (so we can use 'blog:list' in templates)
app_name = 'blog'

urlpatterns = [
    # List all articles: /blog/
    path('', views.article_list, name='list'),
    
    # Single article detail: /blog/my-article-slug/
    path('<slug:slug>/', views.article_detail, name='detail'),
]
