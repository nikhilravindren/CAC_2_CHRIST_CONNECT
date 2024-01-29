from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class user_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ur_landmark = models.CharField(null=True,max_length=100)
    ur_locality = models.CharField(max_length=100,null=True)
    ur_city = models.CharField(max_length=100,null=True)
    ur_state = models.CharField(max_length=100,null=True)
    ur_country = models.CharField(max_length=100,null=True)
    ur_pin = models.IntegerField(null=True)
    ur_phone = models.BigIntegerField(null=True)
    ur_DOB = models.DateField(null=True)
    ur_pic = models.ImageField(upload_to='images/', null=True)
    ur_bio = models.TextField(null=True)
    ur_course = models.CharField(max_length=220,null=True)
    ur_campus = models.CharField(max_length=220,null=True)
class Notifications(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default=0)
    noti_msg = models.CharField(max_length=255)
    noti_status = models.BooleanField(default=1)
    noti_on = models.DateTimeField(default=datetime.datetime.now)

class admin_messages(models.Model):
    msg_from = models.ForeignKey(User, on_delete = models.CASCADE, default=0)
    msg_subject = models.CharField(max_length=255, default=None)
    msg_content = models.CharField(max_length=255)
    msg_on = models.DateTimeField(default=datetime.datetime.now)
    msg_status = models.BooleanField(default=1)



