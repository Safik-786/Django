from django.db import models

class Student(models.Model):
    # stuid=models.IntegerField( primary_key=True)
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stuepass=models.CharField(max_length=70)
    comment=models.CharField(max_length=40, default='not available')

    