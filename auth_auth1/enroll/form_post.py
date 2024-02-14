from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# to adding more field from UserCreationForm class

class SignupForm(UserCreationForm):
    password2= forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields= ['first_name','last_name','email']
        labels= {'email': 'Email', 'first_name':'firstName'}