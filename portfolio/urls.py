from django.urls import path
from .views import homePage, projectpage, addProject, editProject, inboxPage, messagePage




urlpatterns = [
    path('', homePage, name='home'),
    path('project/<str:pk>/', projectpage, name='project'),
    path('add-project/', addProject, name='add-project'),
    path('edit-project/<str:pk>', editProject, name='edit-project'),
    path('inbox/',inboxPage, name='inbox'),
    path('message/<str:pk>/',messagePage, name='message')
    
    
]