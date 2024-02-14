from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# to adding more field from UserCreationForm class

class SignupForm(UserCreationForm):
    # below are the field of the UserCreationForm class
    password2= forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput)


    # below all are the field of the user model
    class Meta:
        model=User
        
        # used to add more fiels
        fields= ['username','first_name','last_name','email']
        
        # used to rename the label name
        labels= {'email': 'Email', 'first_name':'firstName'}
        
        # adding class name to the respective tag
        widgets= {'username' : forms.TextInput(attrs={'class':'form-field safik'}), 'email':forms.EmailInput(attrs={'class':'form-field'})}
        
       