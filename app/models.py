from django.db import models

# Create your models here.

from django.contrib.auth.models import User # by using this command user is table is created
class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()
