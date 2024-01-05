from django.db import models
import uuid
import datetime


# Create your models here.

class JobPortal(models.Model):
    job_id =models.UUIDField(auto_created=True, primary_key=True,default=uuid.uuid4)
    job_postedon=models.DateTimeField(default=datetime.datetime.now())
    job_title=models.TextField(null=False,blank=False, max_length=100)
    company_name=models.TextField(null=False,blank=False, max_length=100)
    job_location=models.TextField(max_length=100)
    job_category=models.TextField(null=False,blank=False)
    job_package=models.TextField(null=False,blank=False)
    job_type=models.TextField(null=False,blank=False)
    job_deadline=models.DateTimeField(blank=True,null=True)
    job_description=models.TextField(null=False,blank=False, max_length=500)





