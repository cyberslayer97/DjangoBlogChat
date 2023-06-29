from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import Author_Profile
from .forms import CustomUserCreationForm, LoginForm, UpdateAuthorForm
from .utils import regis_username, split_tags_author
from django.contrib.auth.models import User

# Create your views here.

def login_profile(request):
    requestuser = request.user.author_profile
    # author_blog = requestuser.blog_set.all()
    # print(author_blog)
    context = {
        'requestuser': requestuser,
        'badge_color': ['primary','secondary','success','danger','warning']

    }
    return render(request, './profile_app/login_profile.html', context)


def profile_setting(request):
    # author_profile_tags = request.user.author_profile.tags.all()

    tags = request.POST.get('tags','')
    t = split_tags_author(tags)

    if request.method == 'POST':
        form = UpdateAuthorForm(request.POST, request.FILES, instance=request.user.author_profile )
        print(form.is_valid())
        if form.is_valid():
            
            instance = form.save(commit=False)

            instance.tags.set(t)
            instance.save()

            return redirect('loginprofile')
        else:
            print(form.errors)
    else:
        form = UpdateAuthorForm(instance=request.user.author_profile)

    context = {
        'form': form,
        # 'tags': initial_tags
    }
    return render(request, './profile_app/profile_settings.html', context)


def login_view(request):
    # print(request.POST)
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    print(request.user)
  
    context = {
        'login_form': LoginForm()
    }
   
    return render(request, './profile_app/login.html', context)



def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
       
        print(form.is_valid())
        if form.is_valid():
            regis_form = form.save(commit=False)
            regis_email = form.cleaned_data['email']
            regis_fullname = form.cleaned_data['Full_name'].lower()
            username, fullname = regis_username(regis_email, regis_fullname)
            if User.objects.filter(username=username).exists():
                form.add_error('email', 'Email already exists')  
            else:            
                regis_form.username = username
                regis_form.first_name = fullname[0]
                regis_form.last_name = fullname[1] if len(fullname) > 1 else ''
                regis_form.save()
                login(request, regis_form)
                return redirect('/')
        
        else:
            print(form.errors.as_text)

    else:
        form= CustomUserCreationForm()
            


    context = {
        'registrations': form,
        # 'form': form,
    }
    return render(request, './profile_app/registration.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

