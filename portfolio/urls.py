from django.urls import path
from .views import homePage, projectpage




urlpatterns = [
    path('', homePage, name='home'),
    path('project/<str:pk>/', projectpage, name='project'),
    
]