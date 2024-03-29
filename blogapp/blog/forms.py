from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post
class SignupForm(UserCreationForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email']
        labels= {'first_name':'First Name', 'last_name':'Last Name', 'email': 'Email'}
        widgets= {
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            }
        
class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput( attrs={'class':'form-control', 'autocomplete': 'current-password'}))
    

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ['author','title', 'description' ]
        widgets= {
            'author':forms.TextInput(attrs={'class': 'form-control'}), 
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditUserProfileForm(UserChangeForm):
    password= None;
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']
        label= {'email':'Email'}  # i change email lebel bocoz it bydefault print email Address
        widgets= {
            'username':forms.TextInput(attrs={'class': 'form-control'}), 
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            
        }
        
