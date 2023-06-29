from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Author_Profile
from blog_app.models import tags

class CustomUserCreationForm(UserCreationForm):
    Full_name = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name','id':"form3Example1c", 'class':"form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':"ID@email.com", 'id':"form3Example3c", 'class':"form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password','placeholder':"Password", 'id':"form3Example4c", 'class':"form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'id':"form3Example4cd", 'class':"form-control"})
    )

    class Meta:
        model = User
        fields = ['Full_name','email', 'password1', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'type':"text", 'id':"form3Example3c" ,'class':"form-control", 'placeholder': 'Username or email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'type':"password", 'id':"form3Example4c", 'class':"form-control", 'placeholder':'Password'})
    )

class UpdateAuthorForm(ModelForm):
    class Meta:
        model = Author_Profile
        exclude = ['user','tags']
        widgets = {
            

            'Authorname': forms.TextInput(attrs={'class':"form-control"}),

            'username': forms.TextInput(attrs={'class':"form-control"}),

            'linkedin': forms.TextInput(attrs={'class':"form-control"}),

            'instagram': forms.TextInput(attrs={'class':"form-control"}),

            'youtube': forms.TextInput(attrs={'class':"form-control"}),

            'twitter': forms.TextInput(attrs={'class':"form-control"}),

            'info': forms.Textarea(attrs={'class':"form-control"}),

            'Profile_image': forms.FileInput(attrs={'class':"form-control mx-auto d-block"}),

        }

        

        