from django.shortcuts import render
from .models import ProjectModel
# Create your views here.


def homePage(request):
    projects = ProjectModel.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})