
from django.db import models
import uuid

# For Adding CKEditor to our project Editing Form.
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.





class Question(models.Model):

    TYPES = (
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('fullstack', 'fullstack'),
    )

    answer = models.CharField(max_length=200, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.answer
    
    
    
    
    

class ProjectModel(models.Model):
    project_title = models.CharField(max_length=200)
    project_thumbnail = models.ImageField(null=True)
    
    # For Adding CKEditor to our project Editing Form.
    project_description = RichTextUploadingField()
    project_slug = models.SlugField(null=True, blank=True)
    project_created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    
    def __str__(self):
        return self.project_title

    
class SkillsModel(models.Model):
    skill_title = models.CharField(max_length=200)
    skill_description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True,default='skill_logo.png')
    skill_created_at = models.DateTimeField(auto_now_add=True)
    skill_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.skill_title
    
    
class SkillsTagModel(models.Model):
    tag_title = models.CharField(max_length=200)
    tag_created_at = models.DateTimeField(auto_now_add=True)
    skill_tag_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.tag_title




class Message(models.Model):
    name = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length = 200, null = True)
    subject = models.CharField(max_length = 200, null = True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body[0:50]