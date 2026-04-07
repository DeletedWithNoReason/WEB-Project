from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
]