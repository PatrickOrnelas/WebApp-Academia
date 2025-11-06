from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
   # path('logout/', views.logout_view, name='logout'),

   # USER
   path('user/register/', views.register_view, name='register'),
]