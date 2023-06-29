from django.contrib import admin
from .models import Blog,tags,Chat
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":["title"]}
    list_display = ("title",)

class ChatAdmin(admin.ModelAdmin):
    list_display = ("group","content","sender")

admin.site.register(Blog, PostAdmin)
admin.site.register(tags)
admin.site.register(Chat, ChatAdmin)