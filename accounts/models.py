from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     ]


class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100)
    age=models.DateField(null=True, blank=True)
    role=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to="profile",null=True,blank=True,max_length=200)
    email=models.EmailField(unique=True)
    phone_no=models.CharField(max_length=12,blank=True,null=True)
    about=models.TextField(max_length=500,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    state=models.CharField(max_length=50,blank=True,null=True)
    zipcode=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    twitter=models.CharField(max_length=100,blank=True,null=True)
    linkedin=models.CharField(max_length=100,blank=True,null=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    instagram=models.CharField(max_length=100,blank=True,null=True)
    # experience = models.TextField(max_length=500, blank=True, null=True)
    # education = models.TextField(max_length=500, blank=True, null=True)




class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    teacher=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    registeration_no=models.AutoField(primary_key=True)                 
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100,blank=True,null=True) 
    age=models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    about=models.TextField(max_length=500,blank=True,null=True)
    profile_image=models.ImageField(upload_to="profile",null=True,blank=True,max_length=200)
    email=models.EmailField(max_length=100,unique=True)
    mobile_no=models.CharField(max_length=12,null=True,blank=True)
    batch=models.IntegerField(null=True,blank=True)
    Course=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    state=models.CharField(max_length=50,blank=True,null=True)
    zipcode=models.CharField(max_length=50,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    twitter=models.CharField(max_length=100,blank=True,null=True)
    linkedin=models.CharField(max_length=100,blank=True,null=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    instagram=models.CharField(max_length=100,blank=True,null=True)
    # education = models.TextField(max_length=500, blank=True, null=True)



class Job(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField(auto_now_add=True)
    

class Gallery(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='gallery_images/',default="",null=True,blank=True)

class Event(models.Model):
    created_by =models.ForeignKey(Teacher,on_delete=models.DO_NOTHING) 
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category=models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)
    
