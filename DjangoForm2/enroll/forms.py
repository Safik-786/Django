from django import forms

class StudendRegistration(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs= {'placeholder':"Entername"}))   
    email= forms.CharField(label="youremail", label_suffix="::",required=True, error_messages={'required':"leaveit"})
    number= forms.IntegerField( disabled=True)
    
class RegdWidget(forms.Form):
    name= forms.CharField()   
    password= forms.CharField(widget=forms.PasswordInput)   
    hidden= forms.CharField(widget=forms.HiddenInput)   
    Browse= forms.CharField(widget=forms.FileInput)   
    text_Area= forms.CharField(widget=forms.Textarea)   
    checkbox= forms.CharField(widget=forms.CheckboxInput)   
    checkbox= forms.CharField(widget=forms.CheckboxInput)   
    Date= forms.CharField(widget=forms.DateInput)   
    # checkboxSelectmulyiple= forms.CharField(widget=forms.CheckboxSelectMultiple) 
    
    # attr
    
    attr= forms.CharField(widget=forms.TextInput(attrs={'class':'safik', "id":'rahul'}))  
    

class FormPost(forms.Form):    
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    price=forms.DecimalField(min_value=5, max_value=40,max_digits=4, decimal_places=1)