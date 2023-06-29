from django.forms import ModelForm
from django import forms
from .models import Blog,tags
from author_profile.models import Author_Profile


class BlogForm(ModelForm):


    class Meta:
        model = Blog
        exclude = ['tags', 'author', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-lg w-100','id':"exampleFormControlInput1",'placeholder':"Write an title"}),

            'content': forms.Textarea(attrs={'class': 'form-control-plaintext form-control-lg border border-dark',  'id':"exampleFormControlTextarea1",'rows':"3"}),

            'image': forms.FileInput(attrs={'class': 'form-control'}),

            # 'slug': forms.TextInput(attrs={'class': 'form-control-lg w-100','id':"exampleFormControlInput1",'placeholder':"URL","type":"hidden"}),

            # 'author': forms.TextInput(attrs={'class':'form-control'}),
            # 'tags': forms.TextInput(attrs={'class':'form-control'}),

        }

# class AuthorForm(ModelForm):
#     # Authorname = forms.TextInput(attrs={'class':'form-control','placeholder':'#Author'})
#     class Meta:
#         model = Author_Profile
#         fields = ['Authorname']
#         widgets = {
#             'Authorname': forms.TextInput(attrs={'class':"form-control form-control-sm",  'placeholder':"#author",
#                 'aria-label':".form-control-sm example",'name':'author'})
#         }

class tagsForm(ModelForm):
    # tagname = forms.TextInput(attrs={'class':'form-control','placeholder':'#Tags'})
    class Meta:
        model = tags
        fields = '__all__'
        widgets = {
            'tagname': forms.TextInput(attrs={'class':"form-control form-control-sm",  'placeholder':"#Tags",
                'aria-label':".form-control-sm example",'name':'tag'})
        }



