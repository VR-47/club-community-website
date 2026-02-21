from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin interface for Article model
    """
    # Auto-generate slug from title
    prepopulated_fields = {'slug': ('title',)}
    
    # Columns shown in list view
    list_display = ('title', 'category', 'author', 'club', 'is_published', 'created_at')
    
    # Filters on the right side
    list_filter = ('category', 'is_published', 'club', 'created_at')
    
    # Search box
    search_fields = ('title', 'summary', 'content', 'author__username')
    
    # Fields shown in edit form (organized in fieldsets)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'summary', 'content')
        }),
        ('Categorization', {
            'fields': ('category', 'club')
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('Publishing', {
            'fields': ('author', 'is_published', 'created_at', 'updated_at')
        }),
    )
    
    # Make created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')
    
    # Show date hierarchy at top
    date_hierarchy = 'created_at'
