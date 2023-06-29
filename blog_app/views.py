from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog,tags,Chat
from author_profile.models import Author_Profile
from django.utils.text import slugify
from .utils import split_tags_author
from .forms import BlogForm,tagsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required(login_url='login')
def index(request):
    new_blogs = Blog.objects.all()[:4]
    context = {
        'new_blogs': new_blogs
    }
    return render(request, './blog_app/index.html', context)

@login_required(login_url='login')
def blogs(request):
    blogs = Blog.objects.all()
    page_num = request.GET.get('page',1)
    paginator = Paginator(blogs,3)

    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    context = {
        'blogs': page_obj,
        'badge_color': ['primary','secondary','success','danger','warning'],
    }
    return render(request, './blog_app/blogs.html', context)



def write_an_article(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        # form1 = AuthorForm(request.POST)
        form2 = tagsForm(request.POST)
        if form.is_valid() and form2.is_valid():
           
            # a1 = form1.cleaned_data['Authorname'].lower()
            t1 = form2.cleaned_data['tagname'].lower()
            tagname = split_tags_author(t1)
            instance = form.save(commit=False)
            instance.slug = slugify(form.cleaned_data['title'])
            instance.author = request.user.author_profile
            instance.save()

            t2 = tags.objects.filter(tagname__in=tagname)
            # a2 = Author_Profile.objects.filter(Authorname__in=authorname)
            instance.tags.set(t2)
            # instance.author.set(a2)
    # print(request.user)
    # print(request.user.author_profile.username)
    
    context = {
        'bform': BlogForm(),
        # 'aform':AuthorForm(),
        'tform':tagsForm()
    }
    return render(request, './blog_app/create_blog.html', context)

def single_blog(request, slug):
    single_blog = Blog.objects.get(slug=slug)
    context = {
        'single_blog': single_blog,
        'badge_color': ['primary','secondary','success','danger','warning']
        }
    return render(request, './blog_app/single_blog.html', context)



@login_required(login_url='login')
def read_later(request):
    try:
        idsession = request.session.get('idsession',[])
        a = request.POST.get('read_later_blog')
        if int(a) not in idsession:
            idsession.append(int(a))
            request.session['idsession'] = idsession
        else:
            print('it is not possible')
        
    except TypeError:
        pass
                
    try:
        b = request.POST.get('remove_read_later_blog')
        print(b)
        if int(b) in idsession:
            idsession.remove(int(b))
            request.session['idsession'] = idsession
        else:
            print('it is not possible')
    except TypeError:
        pass
    

    context = {
        'readlater_blogs': Blog.objects.filter(id__in=idsession)
    }

    return render(request, './blog_app/read_later.html', context)


def rooms(request):
    tag = tags.objects.all()

    context = {
        'tags':tag
    }
    return render(request, './blog_app/rooms.html', context)
    
def room(request, roomname):
    tag = tags.objects.get(tagname=roomname)
    c = Chat.objects.filter(group=tag)

    context = {
        'roomname': roomname,
        'chats':c
    }
    return render(request, './blog_app/room.html',context)


def query(request):
    a = request.POST

    context = {
        'a':a
    }
    return render(request, './blog_app/query.html', context)