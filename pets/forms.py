from django import forms
from .models import Pet

class PetRegisterForm(forms.ModelForm):
    class Meta:
        model= Pet
        fields='__all__'