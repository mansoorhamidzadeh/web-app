from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User, Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']