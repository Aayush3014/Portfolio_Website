# from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import ProjectModel, SkillsModel, SkillsTagModel
from .forms import ProjectForm

def homePage(request):
    projects = ProjectModel.objects.all()
    detailedSkills = SkillsModel.objects.exclude(skill_description="")
    skills = SkillsModel.objects.filter(skill_description="")
    context = {
        'projects':projects,
        'skills':skills,
        'detailedSkills':detailedSkills,
    }
    return render(request, 'portfolio/home.html', context)



def projectpage(request, pk):
    # context = {}
    project = ProjectModel.objects.get(id=pk)
    context = {
        'project':project,
    }
    return render(request, 'portfolio/project.html', context)


def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
    }   
    return render(request, 'portfolio/project_form.html',context)



def editProject(request, pk):
    project = ProjectModel.objects.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
    }   
    return render(request, 'portfolio/project_form.html',context)
    
    