# Generated by Django 4.2.7 on 2024-01-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='ur_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
