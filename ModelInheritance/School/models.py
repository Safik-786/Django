# from django.db import models

# # Create your models here.

# class CommonInfo(models.Model):
#     name= models.CharField(max_length=20)
#     age= models.IntegerField()
#     date= models.DateField()
#     class Meta:
#         abstract= True

# class Student(CommonInfo):
#     # name= models.CharField(max_length=20)
#     # age= models.IntegerField()
#     fees= models.IntegerField()
#     date= None
    
# class Teacher(CommonInfo):
#     # name= models.CharField(max_length=20)
#     # age= models.IntegerField()
#     salary= models.IntegerField()
    
# class Contractor(CommonInfo):
#     # name= models.CharField(max_length=20)
#     # age= models.IntegerField()
#     salary= models.IntegerField()
#     date= models.DateTimeField()            # override

from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommonInfo):
    salary = models.IntegerField()

class Contractor(CommonInfo):
    salary = models.IntegerField()
    date = models.DateTimeField()  # Renamed to avoid conflict

    
    
