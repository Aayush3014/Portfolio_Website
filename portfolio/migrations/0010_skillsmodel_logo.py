# Generated by Django 5.0 on 2024-01-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_rename_msg_body_message_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsmodel',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]