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



#class user_posts(models.Model):
    








