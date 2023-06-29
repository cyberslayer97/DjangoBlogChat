from .models import tags
from author_profile.models import Author_Profile


def split_tags_author(tag):
    tag1 = []

    for t in tag.split():
        check_tags, created = tags.objects.get_or_create(tagname=t)
        tag1.append(check_tags)  


    return tag1