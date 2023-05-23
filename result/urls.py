from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views



urlpatterns=[
    path('home/', views.home,name="home"),
    path('user_contact/', views.user_contact,name="user_contact"),
    path('student/', views.student,name="student"),
    path('addstudent/', views.addstudent,name="add_student"),
    path('student_list/',views.student_list,name="student_list"),
    path('add_course/',views.add_courses,name="add_course"),
    path('add_teachers/',views.add_teacher,name="add_teachers"),
    path('teacher_list/',views.teacher_list,name="teacher_list"),
    path('course_list/',views.course_list,name="course_list"),
    path('classroom/',views.classRoom,name="classroom"),
    path('class_list/',views.classlist,name="class_list"),
    path('makeclassroom/',views.makeclassroom,name="makeclassroom"),
    path('addStdClass/<code>/',views.addStdClass,name="addStdClass"),
    path('classStDelete/<point>/<code>/',views.classStDelete,name="classStDelete"),
    path('StDelete/<p>/',views.StDelete,name="StDelete"),
    path('department/',views.department,name="department"),
    path('course_outcomes/',views.course_outcomes,name="course_outcomes"),
    path('program_outcomes/',views.program_outcomes,name="program_outcomes"),
    path('course_outcomes2/<depname>/',views.course_outcomes2,name="course_outcomes2"),
    path('program_outcomes2/<depname>/',views.program_outcomes2,name="program_outcomes2"),
    path('co_poMapping/',views.co_poMapping,name="co_poMapping"),
    path('co_poMapping2/<depname>/',views.co_poMapping2,name="co_poMapping2"),
    path('co_poMapping3/<depname>/<cc>/',views.co_poMapping3,name="co_poMapping3"),
    path('deleteco_poMapping/<depname>/<cc>/<pk>/',views.deleteco_poMapping,name="deleteco_poMapping"),
    path('imporStdExcel/',views.imporStdExcel,name="imporStdExcel"),
    path('imporCouExcel/',views.imporCouExcel,name="imporCouExcel"),
    path('imporTeacherExcel/',views.imporTeacherExcel,name="imporTeacherExcel"),
    path("resultGreading/",views.resultGreading,name="resultGreading"),
    path("deleteGreading/<pk>/",views.deleteGreading,name="deleteGreading"),
    path('semesters/',views.semesters,name="semesters"),
    path("deletesemester/<pk>/",views.deletesemester,name="deletesemester"),
    path("deleteClass/<id>/",views.deleteClass,name="deleteClass"),
    path("weightx/<x>/",views.weightx,name="weightx"),
    path("upCourse/<x>/",views.upCourse,name="upCourse"),
    path("Deleteadd/<x>/<pk>/<ex>/",views.Deleteadd,name="Deleteadd"),
    path("copo/<depname>/<cc>/",views.copo,name="copo"),
    path("codelete/<depname>/<pk>/",views.codelete,name="codelete"),
    path("roule/",views.roule,name="roule"),
    path("feed/",views.feed,name="feed"),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)