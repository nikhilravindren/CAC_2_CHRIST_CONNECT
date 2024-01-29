# Generated by Django 4.2.7 on 2024-01-28 01:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0013_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_msg', models.CharField(max_length=255)),
                ('done_status', models.BooleanField(default=1)),
                ('done_on', models.DateTimeField(default=datetime.datetime.now)),
                ('done_by', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='done_from', to=settings.AUTH_USER_MODEL)),
                ('done_to', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='done_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]