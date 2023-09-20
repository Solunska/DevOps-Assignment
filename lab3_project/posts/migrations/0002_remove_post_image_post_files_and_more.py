# Generated by Django 4.1.7 on 2023-06-04 19:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='post_files/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='blocked_users',
            field=models.ManyToManyField(blank=True, related_name='blocked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]