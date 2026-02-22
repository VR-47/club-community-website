from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify

class Club(models.Model):
    # FIXED: Changed 'Tech' and 'Sports' to lowercase to match your views.py
    CLUB_TYPES = (
        ('tech', 'Technical & Coding'),
        ('cultural', 'Curricular & Cultural'),
        ('sports', 'Sports & Fitness'),
        ('media', 'Media & Communication')
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    club_type = models.CharField(max_length=20, choices=CLUB_TYPES, default='tech')
    description = models.TextField()
    logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    participants = models.ManyToManyField(User, related_name='events_joined', blank=True)

    def __str__(self):
        return f"{self.title} - {self.club.name}"


class Project(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='projects')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_link = models.URLField(blank=True, null=True, help_text="Link to GitHub, YouTube, or Live Demo")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_projects', blank=True)

    def __str__(self):
        return self.title

class Resource(models.Model):
    # Notice we removed the 'club = models.ForeignKey(...)' line entirely!
    title = models.CharField(max_length=200, help_text="e.g., Django Beginner Notes, Computer Graphics PDF")
    description = models.TextField(blank=True)
    resource_link = models.URLField(help_text="Link to Google Drive, GitHub, etc.")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
      