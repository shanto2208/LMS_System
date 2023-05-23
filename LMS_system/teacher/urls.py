from operator import concat
from django.urls import path
from .import views
from user.views import signup, user_login



urlpatterns=[
    path('teacherHome/', views.teacherHome,name="teacherHome"),
    path("logout/",views.logoutuser,name="logout"),
    path("teachercourse/",views.teachercourse,name="teachercourse"),
    path("teacherresult/<x>/",views.teacherresult,name="teacherresult"),
    path("deleteMark/<x>/<assName>/",views.deleteMark,name="deleteMark"),
    path("weight/<x>/",views.weight,name="weight"),
    path("assesment/<x>/<assName>/",views.assesment,name="assesment"),
    path("profile/",views.profile,name="profile"),
    
    path("updatresult/<x>/<s_id>/<assName>/",views.updatresult,name="updatresult"),
  
]