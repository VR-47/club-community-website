from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Article


def article_list(request):
    """
    Display list of all published articles.
    Can filter by category using ?category=technical (or event_recap, member_achievement)
    """
    # Start with all published articles
    articles = Article.objects.filter(is_published=True)
    
    # Filter by category if provided in URL (e.g., /blog/?category=technical)
    category_filter = request.GET.get('category', '')
    if category_filter:
        articles = articles.filter(category=category_filter)
    
    # Search functionality (optional - searches title and summary)
    search_query = request.GET.get('search', '')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) | 
            Q(summary__icontains=search_query)
        )
    
    context = {
        'articles': articles,
        'current_category': category_filter,
        'search_query': search_query,
    }
    
    return render(request, 'blog/list.html', context)


def article_detail(request, slug):
    """
    Display a single article by its slug.
    URL: /blog/my-article-title/
    """
    article = get_object_or_404(Article, slug=slug, is_published=True)
    
    # Get related articles (same category, excluding current one)
    related_articles = Article.objects.filter(
        category=article.category,
        is_published=True
    ).exclude(id=article.id)[:3]  # Show max 3 related articles
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'blog/detail.html', context)
