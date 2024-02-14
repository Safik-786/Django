from django import forms
from enroll.models import User, UserCollage

class FormPost(forms.Form):    
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    
class StudRegestration(forms.ModelForm):
    class Meta:
        model= User
        # fields= ['name', 'email', 'password']
        # fields= '__all__';
        exclude= ('name',)                   #["name"]
    
    
class StudentRegistration(forms.ModelForm):
    class Meta:
        model= UserCollage
        fields= ['student_name','email', 'password']
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        model= UserCollage
        fields= ['teacher_name','email', 'password']