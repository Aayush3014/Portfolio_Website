# from multiprocessing import context
from django.shortcuts import render
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
    context = {
        'form':form,
    }   
    return render(request, 'portfolio/project_form.html',context)