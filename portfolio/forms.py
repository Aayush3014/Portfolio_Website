from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import ProjectModel, Message, SkillsModel, Comment, Question


class ProjectForm(ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['project_title', 'project_thumbnail', 'project_description']

    def __init__(self, *args, **kwargs):
        
        """The __init__ method is called when an instance of the ProjectForm class is created. 
            The super call ensures that the constructor of the parent class (ModelForm) is also executed. 
            Following that, it customizes the appearance of the form fields by updating the widget attributes 
            for 'project_title' and 'project_description' fields, adding a 'form-control' class."""
            
            
        super(ProjectForm, self).__init__(*args, **kwargs)
            
        self.fields['project_title'].widget.attrs.update(
            {'class': 'form-control'})
        
        """
            self.fields['project_title']: This part refers to the 'project_title' field within the form. In Django forms, 
            each field is represented as an instance of a field class, and you can access them using dictionary-like syntax
            on the fields attribute of the form.

            
            .widget: The .widget attribute of a form field refers to the HTML widget used to render that field in an HTML form. 
            The widget determines how the field is presented on the web page.

            
            .attrs: This is an attribute of the widget that holds a dictionary of HTML attributes for that specific widget.

            
            .update({'class': 'form-control'}): This method updates the dictionary of attributes for the widget.
            In this case, it's adding a new attribute 'class' with the value 'form-control'. 
            The 'form-control' class is commonly used in web development, especially with CSS frameworks like Bootstrap,
            to style form elements and make them visually consistent.
        """

        self.fields['project_description'].widget.attrs.update(
            {'class': 'form-control', })



class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = "__all__"
        exclude = ['is_read']
        
        
    def __init__(self, *args, **kwargs):
            
            
        super(MessageForm, self).__init__(*args, **kwargs)
            
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})


        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })
        
        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control', })
        
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })
        
        
        
class skillsForm(ModelForm):
    
    class Meta:
        model = SkillsModel
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
            
            
        super(skillsForm, self).__init__(*args, **kwargs)
            
        self.fields['skill_title'].widget.attrs.update(
            {'class': 'form-control'})


        self.fields['skill_description'].widget.attrs.update(
            {'class': 'form-control', })


class commentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ['project']
        
        
    def __init__(self, *args, **kwargs):
            
            
        super(commentForm, self).__init__(*args, **kwargs)
            
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})


        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })



class QuestionForm(ModelForm):
    
    class Meta:
        model = Question
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
            
            
        super(QuestionForm, self).__init__(*args, **kwargs)
            
        self.fields['answer'].widget.attrs.update(
            {'class': 'form-control'})