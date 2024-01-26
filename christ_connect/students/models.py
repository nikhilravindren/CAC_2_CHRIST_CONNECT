from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class JobPortal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_postedon = models.DateTimeField(default=datetime.datetime.now)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    job_location = models.CharField(max_length=100)
    job_category = models.CharField(max_length=100)
    job_package = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_deadline = models.DateTimeField(blank=True, null=True)
    job_description = models.TextField(max_length=255, null=False, blank=False)



class user_posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pt_on= models.DateTimeField(default=datetime.datetime.now)
    pt_content = models.TextField(max_length=255, null=True, blank=True)
    pt_media = models.FileField(upload_to='userposts/',null=True,blank=True)
    pt_status=models.BooleanField(default=True)
    pt_likes = models.IntegerField(default=0)
    pt_comment = models.IntegerField(default=0)
    

class post_likes(models.Model):
    post = models.ForeignKey(user_posts, on_delete=models.CASCADE)
    liked_by =models.ForeignKey(User,on_delete=models.CASCADE)
    liked_on =models.DateTimeField(default=datetime.datetime.now)
    like = models.BooleanField(default=False,blank=True,null=True)

class post_comments(models.Model):
    post = models.ForeignKey(user_posts, on_delete=models.CASCADE)
    pt_comment = models.CharField(max_length=225)
    comment_by =models.ForeignKey(User,on_delete=models.CASCADE)
    comment_on =models.DateTimeField(default=datetime.datetime.now)

class user_follow(models.Model):
    followd_by = models.ForeignKey(User,related_name='followed',on_delete=models.CASCADE)
    followd_to = models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE)
    follow_time = models.DateTimeField(default=datetime.datetime.now)
    follow_status = models.BooleanField(default=True,blank=True,null=True)


class messages(models.Model):
    message_by = models.ForeignKey(User,related_name='message_from',on_delete=models.CASCADE)
    message_to = models.ForeignKey(User,related_name='message_for',on_delete=models.CASCADE)
    message = models.CharField(max_length=225)
    message_on = models.DateTimeField(default=datetime.datetime.now)



    








