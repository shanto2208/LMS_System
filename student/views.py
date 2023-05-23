from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from result.views import others_assesment_mark,others_assesments_mark,others_course_assesments_mark,add_student, clsStudent ,clsRoom, add_course

from teacher.models import usersemester,wieght_number,lms_wieght,assesments_mark, wieght_total, weight_ass, gread, AssMark
from result.models import classco,courseCos,copomaping, greading, cos, add_student, add_course, add_teachers, clsRoom, semester, clsStudent, dept, assesment_mark, pos
# Create your views here.

def studentHome(request):
    student_list=add_student.objects.all()
    print(request.session['name'])
    return render(request,"studenthome.html", {'student_list': student_list})

def studentcourse(request):
    email=request.session['name']
    student_list=add_student.objects.all()

    student=student_list.filter(p_email=email)

    for student in student:
        student=student.s_id

    clsRoom_list=clsStudent.objects.all()
    usersemester1=usersemester.objects.all()
    usersemesterx=usersemester1.filter(user_id=student)
    clsRoom_list1=clsRoom_list.filter(stdid=student)
    print(clsRoom_list)
    semester1=semester.objects.all()
    cn=add_course.objects.all()
    clsRoom1=clsRoom.objects.all()
    return render(request,"studentcourse.html",{'clsRoom1':clsRoom1,'clsRoom_list1':clsRoom_list1,'cn':cn , 'semester1':semester1,'usersemesterx':usersemesterx })


def studentResult(request,x):
    email=request.session['name']
    student_list=add_student.objects.all()

    student=student_list.filter(p_email=email)

    for st in student:
        student_id=st.s_id
    print(student_id)

    noti=""
    co_wieght=lms_wieght.objects.all()
    cos_list=cos.objects.all()
    class_list=clsRoom.objects.all()
    course_list=add_course.objects.all()

    weightx=weight_ass.objects.all()
    weightx1=weightx.filter(wieghtClassid=x)
    for weightx2 in weightx1:
        totalweight=weightx2.totalweight
    

    class1=class_list.filter(classCode=x)

    weight0=wieght_number.objects.all()
    weight1=weight0.filter(class_id=x)

    student=clsStudent.objects.all()
    student1=student.filter(classCod=x)
    

    for class2 in class1:
        class3=class2.courseCod
        sec=class2.coursesec
        instructor=class2.instructor
        classSemester=class2.classSemester
        classCode=class2.classCode
    
    course=add_course.objects.all()
    course2=course.filter(courseCode=class3)

    for sub in course2:
        courseName=sub.courseName
        credit=sub.credit
        depname=sub.depname

    cos_list=cos.objects.all()
    cos_list2=cos_list.filter(co_depname=depname)

    courseCos1=courseCos.objects.all()
    courseCos2=courseCos1.filter(courseCos_id=class3)

    teacher=add_teachers.objects.all()
    teacher2=teacher.filter(tCode=instructor)

    for tName in teacher2:
        firstName=tName.tfirstName
        lastName=tName.tlastName


    class4=course_list.filter(courseCode=class3)
    for class5 in class4:
        class6=class5.depname
    co_lis=cos_list.filter(co_depname=class6)
    print(co_lis)
    ass_list=assesments_mark.objects.all()
    exam=ass_list.filter(assid=x)
    weight2=co_wieght.filter(classid=x)

    wieght_number1=wieght_number.objects.all()
    wieght_number2=wieght_number1.filter(class_id=x)

    studentName=add_student.objects.all()
    
    markx=assesment_mark.objects.all()
    mark1=markx.filter(classId=x)

    AssMark1=AssMark.objects.all()
    AssMark2=AssMark1.filter(markClassId=x)

    gread1=gread.objects.all()
    gread2=gread1.filter(greadClassId=x)


    greading1=greading.objects.all()
    

    for g in gread2:
        m=0
        for a in AssMark2:
            if (a.markS_id==g.greadS_id):
                m=float(m)+float(a.MarkAss)
        studentgread=gread.objects.get(id=g.id)
        print(m)  
        studentgread.greadtotalmark=m

        for g1 in greading1:
            if( float(m) >= float(g1.firstMark) and float(m) < float(g1.secMark) ):
                print(g1.greadLetter)
                studentgread.greadLetter=g1.greadLetter
        
        studentgread.save()

    greading1=greading.objects.all()
    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)

    
    #print(exam)
    
    gread1=gread.objects.all()
    gread2=gread1.filter(greadClassId=x)
    return render(request ,'studentResult.html',{'student_id':student_id,'classco2':classco2,'gread2':gread2,'studentName':studentName,'AssMark2':AssMark2,'mark1':mark1,'totalweight':totalweight,'weight1':weight1,'student1':student1,'x':x,'exam':exam,'noti':noti, 'class3':class3, 'sec':sec,
    'firstName':firstName,'lastName':lastName,'courseName':courseName,'credit':credit,
    "classSemester":classSemester,'wieght_number2':wieght_number2})





def studentwieght(request,x):


    others_assesment_mark1=others_assesment_mark.objects.all()
    others_assesment_mark2=others_assesment_mark1.filter(others_classId=x)
    #others_assesment_mark3=others_assesment_mark2.filter(others_assesmentName=assName)
    #others_assesment_mark4=others_assesment_mark3.filter(others_studentId=s_id)
    #others_assesment_mark5=others_assesment_mark4.filter(others_coName="Others")
    

    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    others_assesments_mark3=others_assesments_mark2.filter(others_others_name="Others")


    co_wieght=lms_wieght.objects.all()
    cos_list=cos.objects.all()
    total2=wieght_number.objects.all()
    total=total2.filter(class_id=x)
    
    weightx=weight_ass.objects.all()
    weightx1=weightx.filter(wieghtClassid=x)

    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)
    
    wieght_total1=wieght_total.objects.all()
    wieght_total2=wieght_total1.filter(totalClassid=x)

    class_list=clsRoom.objects.all()
    course_list=add_course.objects.all()
    class1=class_list.filter(classCode=x)

    for class2 in class1:
        class3=class2.courseCod
        sec=class2.coursesec

    courseCos1=courseCos.objects.all()
    courseCos2=courseCos1.filter(courseCos_id=class3)
    #print(courseCos2)
    
    class4=course_list.filter(courseCode=class3)

    for class5 in class4:
        class6=class5.depname

    co_lis=cos_list.filter(co_depname=class6)
    
    ass_list=assesments_mark.objects.all()
    exam=ass_list.filter(assid=x)
    weight2=co_wieght.filter(classid=x)

    noti=""

    return render(request ,'studentwieght.html',{"others_assesments_mark3":others_assesments_mark3,'classco2':classco2,'x':x ,'co_lis':co_lis,'noti':noti, 'class3':class3, 'exam':exam ,'weight2':weight2,'total':total,'sec':sec,'weightx1':weightx1,'courseCos2':courseCos2  })




def studentassesment(request,assName,x):



    

    email=request.session['name']
    student_list=add_student.objects.all()

    student=student_list.filter(p_email=email)

    for st in student:
        student_id=st.s_id
    print(assName)

    others_assesment_mark1=others_assesment_mark.objects.all()
    others_assesment_mark2=others_assesment_mark1.filter(others_classId=x)
    others_assesment_mark3=others_assesment_mark2.filter(others_assesmentName=assName)
    others_assesment_mark4=others_assesment_mark3.filter(others_studentId=student_id)
    others_assesment_mark5=others_assesment_mark4.filter(others_coName="Others")
    




    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=assName)






    ass_list=assesments_mark.objects.all()
    exam=ass_list.filter(assid=x)
    class_list=clsRoom.objects.all()
    class1=class_list.filter(classCode=x)
    for class2 in class1:
        class3=class2.courseCod
        class4=class2.coursesec
        instructor=class2.instructor
        classSemester=class2.classSemester
        classCode=class2.classCode
        
    course=add_course.objects.all()
    course2=course.filter(courseCode=class3)

    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)
    
    
    for sub in course2:
        courseName=sub.courseName
        credit=sub.credit
        depname=sub.depname

    cos_list=cos.objects.all()
    cos_list2=cos_list.filter(co_depname=depname)

    teacher=add_teachers.objects.all()
    teacher2=teacher.filter(tCode=instructor)

    for tName in teacher2:
        firstName=tName.tfirstName
        lastName=tName.tlastName
    
    wieght=lms_wieght.objects.all()
    wieght2=wieght.filter(classid=x)
    weight3=wieght2.filter(asses_name=assName)

    student=clsStudent.objects.all()
    student1=student.filter(classCod=x)

    studentName=add_student.objects.all()

    ass=assesment_mark.objects.all()
    ass1=ass.filter(classId=classCode)
    ass2=ass1.filter(assesmentName=assName)

    courseCos1=courseCos.objects.all()
    courseCos2=courseCos1.filter(courseCos_id=class3)


    return render(request ,'studentassesment.html',{"others_assesments_mark3":others_assesments_mark3,"others_assesment_mark5":others_assesment_mark5,'student_id':student_id,'classco2':classco2,"cos_list2":cos_list2,'studentName':studentName,'x':x, 'assName':assName, 'exam':exam, 'class3':class3,'class4':class4, 'instructor':instructor,"firstName":firstName,"lastName":lastName,'courseName':courseName,'credit':credit,'classSemester':classSemester,'courseCos2':courseCos2,'weight3':weight3,"student1":student1,'cos_list2':cos_list2,'ass2':ass2})

def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully logout!')
    return redirect("signup")

