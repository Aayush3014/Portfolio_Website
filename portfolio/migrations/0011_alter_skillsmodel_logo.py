# Generated by Django 5.0 on 2024-01-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_skillsmodel_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='logo',
            field=models.ImageField(default='skill_logo.png', null=True, upload_to=''),
        ),
    ]
