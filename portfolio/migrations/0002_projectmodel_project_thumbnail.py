# Generated by Django 5.0 on 2023-12-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='project_thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
