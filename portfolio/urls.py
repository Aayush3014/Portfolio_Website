from os import name
from django.urls import path
from .views import homePage, projectpage, addProject, editProject, inboxPage, messagePage, addSkill, votingPage





urlpatterns = [
    path('', homePage, name='home'),
    path('project/<str:pk>/', projectpage, name='project'),
    path('add-project/', addProject, name='add-project'),
    path('edit-project/<str:pk>', editProject, name='edit-project'),
    path('inbox/',inboxPage, name='inbox'),
    path('message/<str:pk>/',messagePage, name='message'),
    path("add-skill/",addSkill,name='add-skill'),
    
    path("chart/",votingPage,name='chart'),
    
    
]