from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clubs.model import Project   

@login_required
def dashboard(request):
    my_projects = Project.objects.filter(student=request.user).order_by('-created_at')
    
    context = {
        'user': request.user,
        'my_projects': my_projects,
        'message': 'Welcome to your student portal!'
    }
    
    return render(request, 'dashboard/index.html', context)


def home(request):
    return render(request, 'dashboard/home.html')


def resources(request):
    return render(request, 'resources.html')
def home(request):
    return render(request, 'home.html')