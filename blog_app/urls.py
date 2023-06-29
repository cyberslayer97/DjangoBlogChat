from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('read-later/', views.read_later, name='read_later'),
    path('create-blog/', views.write_an_article, name='create_blog'),
    path('single-blog/<slug:slug>/', views.single_blog, name='single_blog'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<str:roomname>/', views.room, name='room'),
    path('query/', views.query, name='query'),
]
