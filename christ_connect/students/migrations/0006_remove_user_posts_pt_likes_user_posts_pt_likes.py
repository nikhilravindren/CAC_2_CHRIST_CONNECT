# Generated by Django 4.2.7 on 2024-01-14 10:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0005_alter_user_posts_pt_likes_alter_user_posts_pt_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_posts',
            name='pt_likes',
        ),
        migrations.AddField(
            model_name='user_posts',
            name='pt_likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
