# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}))
    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Renter your Password'}))
    
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')
