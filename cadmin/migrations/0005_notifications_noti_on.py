# Generated by Django 4.2.7 on 2024-01-24 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0004_notifications_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='noti_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
