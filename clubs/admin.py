from django.contrib import admin
from .model import Club, Event, Resource,Project

# This part tells Django Admin how to handle the Club model
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    # This automatically fills the slug field based on the name!
    prepopulated_fields = {'slug': ('name',)}
    
    # These columns will appear in the list view
    list_display = ('name', 'club_type')
    search_fields = ('name',)

# This part handles the Events
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'date', 'is_active')
    list_filter = ('club', 'is_active')
    search_fields = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Shows who made it and for which club right in the main list
    list_display = ('title', 'student', 'club', 'created_at')
    list_filter = ('club',)
    search_fields = ('title', 'student__username')

# This part handles your new Global Resources
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    # Shows the title and when it was added
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)
