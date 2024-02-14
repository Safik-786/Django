from django.db import models
# Create your models here.

class Student(models.Model):
    stuid= models.IntegerField()
    stuname= models.CharField(max_length=70)
    stuemail= models.CharField(max_length=70)
    stuepass= models.CharField(max_length=70)
    
    # def __str__(self) :
    #     # return self.stuname
    #     # return self.stuemail
    #     return str(self.stuid)

class Product(models.Model):
    prodid=models.IntegerField()
    prodname=models.CharField(max_length=50)
    prodprice=models.IntegerField()
    discount=models.IntegerField()
    prodimage= models.ImageField()
