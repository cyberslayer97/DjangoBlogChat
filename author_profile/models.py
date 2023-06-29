from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Authorname = models.CharField(max_length=255)
    Profile_image = models.ImageField(default='user-default.png', upload_to='profile/')
    username = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('blog_app.tags')
    # blogs = models.ManyToManyField('blog_app.Blog')

    def __str__(self):
        return f"{self.Authorname}"