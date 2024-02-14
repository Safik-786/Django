from django import forms

class StudendRegistration(forms.Form):
    name= forms.CharField(initial="Enter Name")   #help_text="fuck"
    email= forms.CharField(required=True)
    number= forms.IntegerField()
    password= forms.CharField()
    key= forms.CharField(widget=forms.HiddenInput())

class StudRegd(forms.Form):
    name= forms.CharField(error_messages={'required':'*Name Cant be empty'},required=True)
    email= forms.EmailField(error_messages={'required':'*Email Cant be empty'},min_length=5,max_length=20)
    password= forms.CharField(error_messages={'required':'*Password Cant be empty'}, widget=forms.PasswordInput(), required=True, min_length=4, max_length=30)
