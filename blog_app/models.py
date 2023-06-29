from django.db import models
from author_profile.models import Author_Profile


class tags(models.Model):
    tagname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tagname}"

class Chat(models.Model):
    group = models.ForeignKey(tags, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(Author_Profile, on_delete=models.SET_NULL, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(default='default.jpg')
    content = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(Author_Profile, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(tags)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"