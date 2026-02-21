from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from clubs.model import Club


class Article(models.Model):
    """
    Blog article model for Technical articles, Event recaps, and Member achievements
    """
    CATEGORY_CHOICES = (
        ('technical', 'Technical Article'),
        ('event_recap', 'Event Recap'),
        ('member_achievement', 'Member Achievement'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    summary = models.CharField(max_length=300, help_text="Short 1-2 sentence summary")
    content = models.TextField(help_text="Full article content")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='technical')
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', help_text="Optional: Link to a club")
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text="Optional cover image")
    is_published = models.BooleanField(default=False, help_text="Only published articles appear on the site")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_category_display_class(self):
        """Return Bootstrap class for category badge"""
        category_classes = {
            'technical': 'bg-primary',
            'event_recap': 'bg-success',
            'member_achievement': 'bg-warning',
        }
        return category_classes.get(self.category, 'bg-secondary')
