from operator import concat
from django.urls import path
from .import views
from user.views import signup, user_login



urlpatterns=[
    path('studentHome/', views.studentHome,name="studentHome"),
    path("logout/",views.logoutuser,name="logout"),
    path("course/",views.course,name="course"),
    path('result/<x>/',views.result,name='studentResult'),

    
    
]