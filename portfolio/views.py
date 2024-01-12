from django.shortcuts import render, redirect
from .models import ProjectModel, SkillsModel, SkillsTagModel, Message, Comment
from .forms import ProjectForm, MessageForm, skillsForm, commentForm
from django.contrib import messages



def homePage(request):
    projects = ProjectModel.objects.all()
    detailedSkills = SkillsModel.objects.exclude(skill_description="")
    skills = SkillsModel.objects.filter(skill_description="")
    
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message is successfully sent.')
    
    context = {
        'projects':projects,
        'skills':skills,
        'detailedSkills':detailedSkills,
        'form':form
    }
    return render(request, 'portfolio/home.html', context)



def projectpage(request, pk):
    project = ProjectModel.objects.get(id=pk)
    count = project.comment_set.count()
    comments = project.comment_set.all().order_by('-created')
    form = commentForm()
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request,'Your message is successfully sent.')
    
    
    context = {
        'project':project,
        'count' : count,
        'comments': comments,
        'form':form,
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
    
    
    
    
    
def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'portfolio/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {
        'message':message
    }
    return render(request, 'portfolio/message.html', context)





def addSkill(request):
    form = skillsForm()
    if request.method == "POST":
        form = skillsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully added a skill.')
            return redirect('home')
            
    context = {
        'form': form
    }
    return render(request, 'portfolio/skill_form.html', context)


def votingPage(request):
    return render(request, 'portfolio/chart.html')