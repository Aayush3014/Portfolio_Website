from django.shortcuts import render
from .models import ProjectModel, SkillsModel, SkillsTagModel
# Create your views here.


def homePage(request):
    projects = ProjectModel.objects.all()
    detailedSkills = SkillsModel.objects.exclude(skill_description="")
    skills = SkillsModel.objects.filter(skill_description="")
    context = {
        'projects':projects,
        'skills':skills,
        'detailedSkills':detailedSkills,
    }
    print(context)
    return render(request, 'portfolio/home.html', context)