from operator import concat
from django.urls import path
from .import views
from user.views import signup, user_login



urlpatterns=[
    path('studentHome/', views.studentHome,name="studentHome"),
    path("logout/",views.logoutuser,name="logout"),
    path("studentcourse/",views.studentcourse,name="studentcourse"),
    path('studentResult/<x>/',views.studentResult,name='studentResult'),
    path('studentwieght/<x>/',views.studentwieght,name='studentwieght'),
    path("studentassesment/<x>/<assName>/",views.studentassesment,name="studentassesment"),

    
    
]