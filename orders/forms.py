from django import forms
from .models import Orders

class Orders_form(forms.ModelForm):
    states=[
       ('AP','Andhra Pradesh'), ('AR','Arunchal Pradesh'),('AS','Assam'),
       ('BR','Bihar'),('CG','Chhattisgarh'), ('GA','Goa'),('GJ','Gujrat'),('HR','Haryana'),
       ('HP','Himanchal Prdesh'),('MP','Madhya Pradesh'), ('MH','Maharashtra'),
       ('MZ','Mizoram'),('NL','Nagaland'),('OD','Odisha'), ('PB','Punjab'),
       ]
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    number=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    country=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    state=forms.ChoiceField(choices=states,widget=forms.Select(attrs={'class':'form-control'}))
    address=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model=Orders
        fields=['first_name','last_name','email','number','country','state','address']