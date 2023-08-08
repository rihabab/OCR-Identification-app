from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('home/', views.home, name="home"),
    path('upload/', views.uploadFile, name="upload"),
    path('logout/', views.logoutUser, name="logout"),
]
