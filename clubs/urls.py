from django.urls import path
from . import views

# This is the namespace we used in Step 1
app_name = 'clubs' 

urlpatterns = [
    # Static paths MUST go first! (This fixes the warning from your master plan)
    path('', views.club_list, name='club_list'), 
    
    # The add_project path MUST have the slug parameter to accept 'coding-club'
    # and MUST have name='add_project'
    path('<slug:club_slug>/add-project/', views.add_project, name='add_project'),
    path('campus/resources/', views.global_resources, name='global_resources'),
    
    
    # Dynamic slug paths (like the detail view) MUST go last
    path('<slug:club_slug>/', views.club_detail, name='club_detail'),
    
    # Feature paths
    path('project/<int:project_id>/like/', views.like_project, name='like_project'),
    path('event/<int:event_id>/register/', views.register_event, name='register_event'),
]