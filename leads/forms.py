from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead
 
 
User = get_user_model()



class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields ='__all__'


    
class CustomUserCreationForm(UserCreationForm):
     class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
        



