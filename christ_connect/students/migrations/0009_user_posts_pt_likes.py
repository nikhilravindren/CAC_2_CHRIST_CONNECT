# Generated by Django 4.2.7 on 2024-01-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_post_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_posts',
            name='pt_likes',
            field=models.IntegerField(default=0),
        ),
    ]