# Generated by Django 4.2.7 on 2024-01-22 12:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0011_follow'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='follow',
            new_name='user_follow',
        ),
    ]
