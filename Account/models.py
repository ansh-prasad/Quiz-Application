from django.db import models
from  django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    email_address = models.CharField(max_length=50 , unique=True , null=True)
    bio = models.TextField(blank=True , null=True)
    profile_img = models.ImageField(upload_to='profile_images' , default='1.jpg' , blank=True , null=True)
    location = models.CharField(max_length=100 , null=True , blank=True)
    GENDER = (
        ('Male' , 'Male'),
        ('Female' , 'Female'),
    )
    gender = models.CharField(max_length=6 , choices=GENDER , blank=True , null=True)