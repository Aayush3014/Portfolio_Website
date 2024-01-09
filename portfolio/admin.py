from django.contrib import admin
from portfolio.models import ProjectModel, SkillsModel, SkillsTagModel, Message
# Register your models here.

admin.site.register(ProjectModel)
admin.site.register(SkillsModel)
admin.site.register(SkillsTagModel)
admin.site.register(Message)