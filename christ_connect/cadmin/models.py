from django.db import models
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



