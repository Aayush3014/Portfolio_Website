# Generated by Django 5.0 on 2024-01-09 10:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_skillsmodel_skill_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='project_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
