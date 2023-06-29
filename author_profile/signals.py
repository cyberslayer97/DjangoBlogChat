from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author_Profile


@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Authorname = user.first_name + ' ' + user.last_name
        Author_username = user.username
        auth_profile = Author_Profile.objects.create(user=user, Authorname=Authorname, username=Author_username)
        auth_profile.save()


# @receiver(post_save, sender=Author_Profile)
# def update_author_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.user.save()