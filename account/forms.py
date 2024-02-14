from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User


class User_registration(forms.ModelForm):
    password1=forms.CharField(label="Confirm Password" ,widget=forms.PasswordInput)
    password=forms.CharField( widget=forms.PasswordInput)
    
    class Meta :
        model=User
        fields=['username','password' ,'password1','first_name','last_name','email']
    
    def clean(self):
        data=self.cleaned_data
        print(data,"--------")
        pwd1=self.cleaned_data.get("password")
        pwd2=self.cleaned_data.get("password1")
        if pwd1!=pwd2:
            raise forms.ValidationError("Password must be same")
        return data

    def clean_email(self):
       
      
        email=self.cleaned_data.get("email")
        is_exists=User.objects.filter(email=email).exists()
        
        if is_exists:
            raise forms.ValidationError("Kindly Enter different Email")
        return email