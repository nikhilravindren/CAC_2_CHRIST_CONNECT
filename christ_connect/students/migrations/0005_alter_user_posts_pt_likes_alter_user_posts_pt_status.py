# Generated by Django 4.2.7 on 2024-01-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_user_posts_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='pt_likes',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user_posts',
            name='pt_status',
            field=models.BooleanField(default=True),
        ),
    ]
