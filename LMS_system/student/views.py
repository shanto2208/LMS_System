from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from result.views import add_student, clsStudent ,clsRoom, add_course
from result.models import duptclsRoom

# Create your views here.

def studentHome(request):
    student_list=add_student.objects.all()
    print(request.session['name'])
    return render(request,"studenthome.html", {'student_list': student_list})

def course(request):
    newclass_list=duptclsRoom.objects.all()
    for newcls in newclass_list:
        newcls.delete()
    x=request.session['name']
    student_list=add_student.objects.all()
    newclass_list=duptclsRoom.objects.all()
    student=student_list.filter(p_email=x)
    for std in student:
        id=std.s_id
        cn=add_course.objects.all()
        class_list=clsStudent.objects.all()
        st=class_list.filter(stdid=id)
        for cls in st:
            xx=cls.classCod
            all_class=clsRoom.objects.all()
            classroom=all_class.filter(classCode=xx)

            for newcls in classroom:

                cls=cn.filter(courseCode=newcls.courseCod)
                print(newcls.courseCod)
                for cl in cls: 
                    print(cl.courseName)
                    cc=cl.courseName
                    newclass_list.dupclassName=cc
                    newclass_list.dupclassCode=newcls.classCode
                    newclass_list.dupclassSemester=newcls.classSemester
                    newclass_list.dupcourseCod=newcls.courseCod
                    newclass_list.dupcoursesec=newcls.coursesec
                    newclass_list.dupinstructor=newcls.instructor
                    newclass_list.duptClassTime=newcls.tClassTime
                    newclass_list.duplabClassTime=newcls.labClassTime
                    new_add=duptclsRoom(dupclassCode=newclass_list.dupclassCode, dupclassSemester=newclass_list.dupclassSemester,dupcourseCod=newclass_list.dupcourseCod,dupcoursesec=newclass_list.dupcoursesec,dupinstructor=newclass_list.dupinstructor,duptClassTime=newclass_list.duptClassTime,duplabClassTime=newclass_list.duplabClassTime,dupclassName=newclass_list.dupclassName)
                    new_add.save()
    newclass_list=duptclsRoom.objects.all()

    return render(request,"courses.html",{'newclass_list':newclass_list,'cn':cn } )


def result(request,x):



    return render(request,"result.html",{'x':x} )






def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully logout!')
    return redirect("signup")

