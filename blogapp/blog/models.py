from django.db import models

# Create your models here.

class Post(models.Model):
    author= models.CharField(max_length= 150)
    title= models.CharField(max_length= 150)
    description= models.TextField()
    
class PostwithImage(models.Model):
    author= models.CharField(max_length= 150)
    title= models.CharField(max_length= 150)
    description= models.TextField()
    blog_image= models.ImageField(upload_to='blogimg')

    
