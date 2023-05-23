from operator import concat
from django.urls import path
from .import views



urlpatterns=[
    path('', views.signup,name="signup"),
    path('login/', views.user_login,name="login"),
    path('contact/', views.contact,name="contact"),
    path('user_signup/', views.user_signup,name="user_signup"),
    path('user_login/', views.login,name="user_login"),
    
]