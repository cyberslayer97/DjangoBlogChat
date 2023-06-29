from django.contrib.auth.models import User
from blog_app.models import tags


def regis_username(e,f):
    fullname = f.split()

    return e.split('@')[0], fullname




def split_tags_author(tag):
    tag1 = []

    for t in tag.split():
        check_tags, created = tags.objects.get_or_create(tagname=t)
        tag1.append(check_tags)  


    return tag1