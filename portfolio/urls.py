from django.urls import path
from .views import homePage, projectpage, addProject, editProject




urlpatterns = [
    path('', homePage, name='home'),
    path('project/<str:pk>/', projectpage, name='project'),
    path('add-project/', addProject, name='add-project'),
    path('edit-project/<str:pk>', editProject, name='edit-project'),
]