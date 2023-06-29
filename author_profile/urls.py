from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_profile, name='loginprofile'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.profile_setting, name='profile_settings'),

    
]
