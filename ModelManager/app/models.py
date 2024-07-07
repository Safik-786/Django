from django.db import models
from .managers import CustomManager


# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=20)
    roll= models.IntegerField()
    age= models.IntegerField()
    
    students= CustomManager()
    objects= models.Manager()
    
    
