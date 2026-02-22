from django.shortcuts import redirect, render, get_object_or_404
from .model import Club, Project, Event , Resource
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def club_list(request):
    """
    Fetches all clubs from the database.
    """
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})

def club_detail(request, club_slug):
    """
    Fetches a single club.
    If the club_type is 'tech', it loads a special coding template.
    Otherwise, it loads the standard club template.
    """
    club = get_object_or_404(Club, slug=club_slug)
    
    # Logic to choose the right template based on club type
    if club.club_type == 'tech':
        template_name = 'clubs/detail_coding.html'
    elif club.club_type == 'sports':
        template_name = 'clubs/detail_sports.html'
    else:
        template_name = 'clubs/detail_generic.html'

    return render(request, template_name, {'club': club})

@login_required
def add_project(request, club_slug):
    # Find the club based on the URL slug
    club = get_object_or_404(Club, slug=club_slug)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.student = request.user
            project.club = club
            project.save()
            # Redirect back to the club page or dashboard
            return redirect('clubs:club_detail', club_slug=club.slug)
    else:
        form = ProjectForm()

    # Create a simple template or pass it to an existing one
    return render(request, 'clubs/add_project.html', {'form': form, 'club': club})

@login_required
def like_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user in project.likes.all():
        project.likes.remove(request.user)
    else:
        project.likes.add(request.user)
    return redirect('clubs:club_detail', club_slug=project.club.slug)

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)
    return redirect('clubs:club_detail', club_slug=event.club.slug)



def global_resources(request):
    # Fetch ALL resources in the database, newest first
    resources = Resource.objects.all().order_by('-uploaded_at')
    
    return render(request, 'clubs/global_resources.html', {'resources': resources})

