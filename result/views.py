
# from multiprocessing import context
from django.shortcuts import render
from .models import pOAttainment,classcopomaping,classPo,coursePos,teachersFeadback,coAttainment,others_assesment_mark,others_assesments_mark,others_course_assesments_mark,course_weight_ass,course_wieght_total,course_lms_wieght,course_wieght_number,course_assesments_mark,classco,courseCos,copomaping, greading, cos, add_student, add_course, add_teachers, clsRoom, semester, clsStudent, dept, assesment_mark, pos
from teacher.models import rouleW,usersemester,wieght_number,lms_wieght,assesments_mark, wieght_total, weight_ass, gread, AssMark
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect

from tablib import Dataset
from .resources import studentResource, courseResource, teacherResource
# pip install django-import-export
# pip install fontawesomefree
# pip install django-chartjs


def imporStdExcel(request):
    if request.method == "POST":
        student_Resource = studentResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = add_student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
            )
            value.save()
            noti = 1

    return render(request, 'exStudent.html',)


def imporTeacherExcel(request):
    noti = 0
    if request.method == "POST":
        Teacher_Resource = teacherResource()
        dataset = Dataset()
        new_teacher = request.FILES['myfile']
        imported_data = dataset.load(new_teacher.read(), format='xlsx')
        for data in imported_data:
            value = add_teachers(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
            )
            value.save()
            noti = 1

    return render(request, 'exTeacher.html', {'noti': noti})


def imporCouExcel(request):
    if request.method == "POST":
        course_Resource = courseResource()
        dataset = Dataset()
        new_course = request.FILES['myfile']
        imported_data = dataset.load(new_course.read(), format='xlsx')
        for data in imported_data:
            value = add_course(
                data[0],
                data[1],
                data[2],
                data[3]


            )
            value.save()

    return render(request, 'exCourse.html')


# Create your views here.

def resultGreading(request):
    gread_noti = 0
    flag = 0
    greading1 = greading.objects.all()
    if request.method == "POST":
        firstMark = request.POST['firstMark']
        secMark = request.POST['secMark']
        greadLetter = request.POST['greadLetter']
        gpa = request.POST["gpa"]
        gpa = float(gpa)
        gread_noti = 0
        if (firstMark != secMark):
            gread_noti = 2
            if (greading.objects.all()):
                for g in greading1:

                    if (float(g.gpa) == float(gpa) or g.greadLetter == greadLetter):
                        gread_noti = 0
                        flag = 0
                        break
                    elif (int(g.firstMark) == int(firstMark) or int(g.secMark) == int(secMark)):
                        flag = 0
                        print(1)
                        break

                    else:
                        if (int(g.firstMark) < int(firstMark) and int(g.secMark) > int(firstMark)):
                            flag = 0
                            print(2)
                            break
                        else:
                            if (int(g.firstMark) < int(firstMark) and int(g.secMark) > int(secMark)):
                                flag = 0
                                print(3.1)
                                break
                            elif (int(g.firstMark) < int(secMark) and int(g.secMark) > int(secMark)):
                                flag = 0
                                print(3.1)
                                break
                            else:
                                print(g.firstMark +"<"+ firstMark +"and"+ g.secMark +">"+ secMark)
                                flag = flag+1
                                print(flag)
                            

            else:
                gread_noti = 1
                addgreading = greading(
                    firstMark=firstMark, secMark=secMark, greadLetter=greadLetter, gpa=gpa)
                addgreading.save()
                greading1 = greading.objects.all()
        else:
            gread_noti = 2
        if (flag > 0):
            gread_noti = 1
            addgreading = greading(
                firstMark=firstMark, secMark=secMark, greadLetter=greadLetter, gpa=gpa)
            addgreading.save()
            greading1 = greading.objects.all()
        return render(request, 'greading.html', {"greading1": greading1, 'flag': flag, 'gread_noti': gread_noti})

    return render(request, 'greading.html', {"greading1": greading1})


def deleteGreading(request, pk):
    greading1 = greading.objects.get(id=pk)
    greading1.delete()
    return redirect('resultGreading')


def home(request):
    student1 = add_student.objects.all()
    course1 = add_course.objects.all()
    teacher1 = add_teachers.objects.all()
    student = add_student.objects.all().count()
    teacher = add_teachers.objects.all().count()
    course = add_course.objects.all().count()


    dept1 = dept.objects.all()
    semester1 = semester.objects.all()
    for x in semester1:
        same = semester.objects.get(id=x.id)
        same.studentamount = student1.filter(seme=x.semester).count()
        same.save()

    for d in dept1:
        same = dept.objects.get(id=d.id)
        
        same.dep_numberOfstudent = student1.filter(dep=d.dept_name).count()
        same.dep_numberOfCourse = course1.filter(depname=d.dept_name).count()
        same.dep_numberOfTeacher = teacher1.filter(tdep=d.dept_name).count()

        print(same.dep_numberOfstudent)

        same.save()

    dept1 = dept.objects.all()
    semester1 = semester.objects.all()

    return render(request, 'home.html', {"student": student, "teacher": teacher, "course": course, 'student1': student1, 'semester1': semester1, 'dept1': dept1})


def user_contact(request):
    return render(request, 'user_contact.html')


def student(request):
    return render(request, 'add_page.html')


def classRoom(request):

    return render(request, 'Classroom.html')


def classStDelete(request, point, code):

    stu_list = clsStudent.objects.all()
    print(point)

    student = stu_list.filter(id=point)
    for std in student:
        studentId = std.stdid
        code = std.classCod
        student_list = stu_list.filter(classCod=code)
        addstudent_noti = 4
        student.delete()

    gread1 = gread.objects.all()
    gread2 = gread1.filter(greadClassId=code)
    gread3 = gread2.filter(greadS_id=studentId)
    gread3.delete()

    AssMark1 = AssMark.objects.all()
    AssMark2 = AssMark1.filter(markClassId=code)
    AssMark3 = AssMark2.filter(markS_id=studentId)
    AssMark3.delete()

    coStudent = assesment_mark.objects.all()
    coStudent1 = coStudent.filter(studentId=studentId)
    coStudent1.delete()

    class_list = clsRoom.objects.all()
    student_list = clsStudent.objects.all()
    student_list = student_list.filter(classCod=code)

    return redirect("addStdClass", code,)


def classlist(request):
    class_list = clsRoom.objects.all()


    return render(request, 'class_list.html', {'class_list': class_list})


def addStdClass(request, code):
    addstudent_noti = 10
    student_list = clsStudent.objects.all()

    if request.method == "POST":
        classcod = code
        Stdid = request.POST["stdid"]
        student = student_list.filter(classCod=classcod)
        addstudent_noti = 0
        std = add_student.objects.all()
        std1 = std.filter(s_id=Stdid)
        if (std.filter(s_id=Stdid)):
            if len(Stdid) == 13:
                for stud in student:
                    if stud.classCod == code:
                        if stud.stdid == Stdid:
                            print("pass are same")
                            addstudent_noti = 1
                if (addstudent_noti == 0):

                    addStdCls = clsStudent(stdid=Stdid, classCod=classcod)
                    addStdCls.save()
                    coStudent = assesment_mark.objects.all()

                    AssMark1 = AssMark.objects.all()
                    AssMark2 = AssMark1.filter(markClassId=code)

                    gread1 = gread.objects.all()
                    greadS_id = Stdid
                    greadClassId = classcod
                    greadtotalmark = 0
                    greadLetter = "#"
                    addgread = gread(greadS_id=greadS_id, greadClassId=greadClassId,
                                     greadtotalmark=greadtotalmark, greadLetter=greadLetter)
                    addgread.save()

                    dep1 = clsRoom.objects.all()
                    dep2 = dep1.filter(classCode=code)

                    for id in dep2:
                        seme=id.classSemester


                    usersemester1=usersemester.objects.all()
        
                    usersemesterx=usersemester1.filter(user_id=Stdid)
                    usersemester2=usersemester1.filter(user_id=Stdid).count()
                    usersemester3=usersemesterx.filter(semestername=seme).count()

                    if(usersemester2>0):
                        
                        if(usersemester3==0):
                            user_id=Stdid
                            semestername=seme 
                            adduser=usersemester(user_id=user_id,semestername=semestername)
                            adduser.save()
                    else:
                        user_id=Stdid
                        semestername=seme 
                        adduser=usersemester(user_id=user_id,semestername=semestername)       
                        adduser.save()


                    for dep3 in dep2:
                        courseCode = dep3.courseCod
                        dep4 = add_course.objects.all()
                        dep5 = dep4.filter(courseCode=courseCode)
                        for dep6 in dep5:
                            dep = dep6.depname
                    cos_list = cos.objects.all()
                    cos_list1 = cos_list.filter(co_depname=dep)
                    classco1=classco.objects.all()
                    classco2=classco1.filter(classId=code)

                    ass = assesments_mark.objects.all()
                    ass1 = ass.filter(assid=code)
                    for ass2 in ass1:
                        assesmentName = ass2.ass_name
                        markS_id = Stdid
                        markClassId = code
                        markAssName = assesmentName
                        MarkAss = 0
                        addAssMark = AssMark(
                            markS_id=markS_id, markClassId=markClassId, markAssName=markAssName, MarkAss=MarkAss)
                        addAssMark.save()

                        for co in classco2:
                            classId = code
                            studentId = Stdid
                            assesmentName = assesmentName
                            coName = co.classCosname
                            mark = 0.0
                            addassesment_mark = assesment_mark(
                                classId=classId, studentId=studentId, assesmentName=assesmentName, coName=coName, mark=mark)
                            addassesment_mark.save()

                        others_classId= code
                        others_studentId= Stdid
                        others_assesmentName=assesmentName
                        others_coName="Others"
                        others_mark=0
                        addcothers=others_assesment_mark(others_classId=others_classId,others_studentId=others_studentId,others_assesmentName=others_assesmentName,others_coName=others_coName,others_mark=others_mark)
                        addcothers.save()
                # cos1=cos_list.filter(co_depname=)
        else:
            print("id wrong")
            addstudent_noti = 3

    student_list = student_list.filter(classCod=code)
    return render(request, 'addStdClass.html', {'code': code, 'student_list': student_list, 'addstudent_noti': addstudent_noti})


def makeclassroom(request):
    semester_list = semester.objects.all()
    teacher_list = add_teachers.objects.all()
    course_list = add_course.objects.all()
    class_list = clsRoom.objects.all()
    classco1=classco.objects.all()
    courseCos1=courseCos.objects.all()

    

    if request.method == "POST":
        
        classSemester = request.POST["classSemester"]
        courseCod = request.POST["courseCod"]
        coursesec = request.POST["coursesec"]
        instructor = request.POST["instructor"]
        tClassTime = request.POST["tClassTime"]
        labClassTime = request.POST["labClassTime"]
        classCode = classSemester+coursesec+courseCod

        usersemester1=usersemester.objects.all()
        
        usersemesterx=usersemester1.filter(user_id=instructor)
        usersemester2=usersemester1.filter(user_id=instructor).count()
        usersemester3=usersemesterx.filter(semestername=classSemester).count()

        if(usersemester2>0):
            
            if(usersemester3==0):
                user_id=instructor
                semestername=classSemester 
                adduser=usersemester(user_id=user_id,semestername=semestername)
                adduser.save()
        else:
            user_id=instructor
            semestername=classSemester 
            adduser=usersemester(user_id=user_id,semestername=semestername)       
            adduser.save()

        coursePos1=coursePos.objects.all()
        coursePos2=coursePos1.filter(coursePos_id=courseCod)

        courseCos2=courseCos1.filter(courseCos_id=courseCod)
        for c1 in courseCos2:
            classId=classCode
            classCosname=c1.courseCosname
            classCosmark=c1.courseCosmark

            addclassCo=classco(classId=classId,classCosname=classCosname,classCosmark=classCosmark)

            addclassCo.save()

        

        copomaping1=copomaping.objects.all()
        copomaping2=copomaping1.filter(copomapingCc= courseCod)


        for p in coursePos2:
            classPoId=classCode
            classPosname=p.coursePosname
            x=0
            copomaping3=copomaping2.filter(copomapingpo=classPosname)

            for co in copomaping3:
                coname=co.copomapingCo
                courseCos3=courseCos2.filter(courseCosname=coname)
                for po in courseCos3:
                    x=float(x)+ float(po.courseCosmark)
            classPosmark=x
            addcp=classPo(classPoId=classPoId,classPosname=classPosname,classPosmark=classPosmark)
            addcp.save()


        for co in copomaping2:
            copomapingCc=classCode
            copomapingCo=co.copomapingCo
            copomapingpo=co.copomapingpo
            addco=classcopomaping(copomapingCc=copomapingCc, copomapingCo=copomapingCo, copomapingpo=copomapingpo)
            addco.save()

        if( class_list.filter(classCode=classCode) ):

            noti=0

        else:

            addclass = clsRoom(classCode=classCode, classSemester=classSemester, courseCod=courseCod,
                           coursesec=coursesec, instructor=instructor, tClassTime=tClassTime, labClassTime=labClassTime)
            
            addclass.save()



            assesment=assesments_mark.objects.all()
            assesment2=assesment.filter(assid=classCode)

            weight1=lms_wieght.objects.all()
            weight2=weight1.filter(classid=classCode)
            
            wieghtNumber=wieght_number.objects.all()
            wieghtNumber2=wieghtNumber.filter(class_id=classCode)
            
            mark=assesment_mark.objects.all()
            mark2=mark.filter(classId=classCode)
            
            AssMark1=AssMark.objects.all()
            AssMark2=AssMark1.filter(markClassId=classCode)

            weight_ass1=weight_ass.objects.all()
            weight_ass2=weight_ass1.filter(wieghtClassid=classCode)

            others_assesments_mark1=others_assesments_mark.objects.all()

            
            

            x=courseCod

            course_assesments_mark1=course_assesments_mark.objects.all()
            course_assesments_mark2=course_assesments_mark1.filter(course_assid=x)
            
            course_wieght_number1=course_wieght_number.objects.all()
            course_wieght_number2=course_wieght_number1.filter(course_class_id=x)
            
            others_course_assesments_mark1=others_course_assesments_mark.objects.all()
            others_course_assesments_mark2=others_course_assesments_mark1.filter(others_course_assid=x)

            course_lms_wieght1=course_lms_wieght.objects.all()
            course_lms_wieght2=course_lms_wieght1.filter(course_classid=x)

            course_wieght_total1=course_wieght_total.objects.all()
            course_wieght_total2=course_wieght_total1.filter(totalClassid=x)

            course_weight_ass1=course_weight_ass.objects.all()
            course_weight_ass2=course_weight_ass1.filter(wieghtClassid=x)

            


            for course_assesments_mark3 in course_assesments_mark2:
                assid=classCode
                ass_name=course_assesments_mark3.course_ass_name
                ass_point=course_assesments_mark3.course_ass_point
                addcourse_assesments_mark3=assesments_mark(assid=assid,ass_name=ass_name,ass_point=ass_point)
                addcourse_assesments_mark3.save()


            for course_wieght_number3 in course_wieght_number2:
                class_id=classCode
                Exam_name=course_wieght_number3.course_Exam_name
                wieght=course_wieght_number3.course_wieght
                taken=course_wieght_number3.course_taken
                ratio=course_wieght_number3.course_ratio
                addcourse_wieght_number3=wieght_number(class_id=class_id,Exam_name=Exam_name,wieght=wieght,taken=taken,ratio=ratio )
                addcourse_wieght_number3.save()


            for course_lms_wieght3 in course_lms_wieght2:

                classid=classCode
                asses_name=course_lms_wieght3.course_asses_name
                co_name=course_lms_wieght3.course_co_name
                asses_point=course_lms_wieght3.course_asses_point
                addcourse_lms_wieght3=lms_wieght(classid=classid,asses_name=asses_name,co_name=co_name,asses_point=asses_point  )
                addcourse_lms_wieght3.save()

            for course_wieght_total3 in course_wieght_total2:
                totalClassid=classCode
                totalAsses_name=course_wieght_total3.totalAsses_name
                totalCo_name=course_wieght_total3.totalCo_name
                totalpoint=course_wieght_total3.totalpoint
                addcourse_wieght_total3=wieght_total(totalClassid=totalClassid,totalAsses_name=totalAsses_name,totalCo_name=totalCo_name,totalpoint=totalpoint  )
                addcourse_wieght_total3.save()


            for course_weight_ass3 in course_weight_ass2:
                wieghtClassid=classCode
                totalweight=course_weight_ass3.totalweight
                addweight_ass=weight_ass(wieghtClassid=wieghtClassid,totalweight=totalweight)
                addweight_ass.save()

            for others_course_assesments_mark3 in others_course_assesments_mark2:
                others_assid=classCode
                others_ass_name=others_course_assesments_mark3.others_course_ass_name
                others_others_name=others_course_assesments_mark3.others_course_others_name
                others_ass_point=others_course_assesments_mark3.others_course_ass_point
                addothers_course_assesments_mark=others_assesments_mark(others_assid=others_assid,others_ass_name=others_ass_name,others_others_name=others_others_name,others_ass_point=others_ass_point)
                addothers_course_assesments_mark.save()



            cos1 =cos.objects.all()

            course_list1=course_list.filter(courseCode=courseCod)

            for course_list2 in course_list1:
                dep=course_list2.depname

            print(dep)

            cos2=cos1.filter(co_depname=dep)

            for cos3 in cos2:
                coAttainmentId=classCode
                coAttainmentCosname=cos3.co_name
                coAttainmentCosmark=0
                coAttainmentAttainment=0

                addat=coAttainment(coAttainmentId=coAttainmentId,coAttainmentCosname=coAttainmentCosname,coAttainmentCosmark=coAttainmentCosmark, coAttainmentAttainment=coAttainmentAttainment)
                addat.save()

            pos1 =pos.objects.all()
            pos2=pos1.filter(po_depname=dep)

            for pos3 in pos2:
                poAttainmentId=classCode
                poAttainmentCosname=pos3.po_name
                poAttainmentCosmark=0
                poAttainmentAttainment=0

                addat=pOAttainment(pOAttainmentId=poAttainmentId,pOAttainmentCosname=poAttainmentCosname,pOAttainmentCosmark=poAttainmentCosmark, pOAttainmentAttainment=poAttainmentAttainment)
                addat.save()

            class_list = clsRoom.objects.all()
            weightx = weight_ass.objects.all()
            wieghtClassid = classCode
            return redirect("class_list")
    # render(request ,'makeClassroom.html',{'semester_list': semester_list})
    return render(request, 'makeClassroom.html', {'semester_list': semester_list, 'teacher_list': teacher_list, 'course_list': course_list})


def deleteClass(request,id):

    class_list = clsRoom.objects.all()
    weightx = weight_ass.objects.all()
    class_list1=class_list.filter(classCode=id)
    weightx1=weightx.filter(wieghtClassid=id)
    class_list1.delete()
    weightx1.delete()

    classcopomaping1=classcopomaping.objects.all()
    classcopomaping2=classcopomaping1.filter(copomapingCc=id)
    classcopomaping2.delete()

    classPo1=classPo.objects.all()
    classPo2=classPo1.filter(classPoId=id)
    classPo2.delete()


    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=id)

    others_assesments_mark2.delete()

    gread1 = gread.objects.all()
    gread2 = gread1.filter(greadClassId=id)
    gread2.delete()

    classco1=classco.objects.all()
    classco2=classco1.filter(classId=id)
    classco2.delete()

    AssMark1 = AssMark.objects.all()
    AssMark2 = AssMark1.filter(markClassId=id)
  
    AssMark2.delete()

    coStudent = assesment_mark.objects.all()
    coStudent1 = coStudent.filter(classId=id)
    coStudent1.delete()

    class_list = clsRoom.objects.all()
    student_list = clsStudent.objects.all()
    student_list1 = student_list.filter(classCod=id)
    student_list1.delete()
    
    assesments_mark1=assesments_mark.objects.all()
    assesments_mark2=assesments_mark1.filter(assid=id)
    assesments_mark2.delete()

    lms_wieght1=lms_wieght.objects.all()
    lms_wieght2=lms_wieght1.filter(classid=id)
    lms_wieght2.delete()

    wieght_number1=wieght_number.objects.all()
    wieght_number2=wieght_number1.filter(class_id=id)
    wieght_number2.delete()

    wieght_total1=wieght_total.objects.all()
    wieght_total2=wieght_total1.filter(totalClassid=id)
    wieght_total2.delete()

    weight_ass1=weight_ass.objects.all()
    weight_ass2=weight_ass1.filter(wieghtClassid=id)
    weight_ass2.delete()

    AssMark1=AssMark.objects.all()
    AssMark2=AssMark1.filter(markS_id=id)
    AssMark2.delete()

    gread1=gread.objects.all()
    gread2=gread1.filter(greadS_id=id)
    gread2.delete()

    others_assesment_mark1= others_assesment_mark.objects.all()
    others_assesment_mark1=others_assesment_mark1.filter(others_classId=id)
    others_assesment_mark1.delete()


    coAttainment1=coAttainment.objects.all()
    coAttainment2=coAttainment1.filter(coAttainmentId=id)
    coAttainment2.delete()


    pOAttainment1=pOAttainment.objects.all()
    pOAttainment2=pOAttainment1.filter(pOAttainmentId=id)
    pOAttainment2.delete()


    return redirect("class_list")



def addstudent(request):
    dep_noti = 3
    student = add_student.objects.all()
    dept_list = dept.objects.all()
    semester_list = semester.objects.all()
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        s_id = request.POST["s_id"]
        gender = request.POST["gender"]
        p_email = request.POST["p_email"]
        phone = request.POST["phone"]
        dep = request.POST["dep"]
        seme = request.POST['seme']
        if (student.filter(p_email=p_email)):
            dep_noti = 0
            return render(request, 'add_student.html', {'semester_list': semester_list, 'dept_list': dept_list, 'dep_noti': dep_noti})
        else:
            if (student.filter(s_id=s_id)):
                dep_noti = 2
                return render(request, 'add_student.html', {'semester_list': semester_list, 'dept_list': dept_list, 'dep_noti': dep_noti})
            else:
                dep_noti = 1
                add = add_student(firstName=firstName, lastName=lastName, s_id=s_id,
                                  gender=gender, p_email=p_email, phone=phone, dep=dep, seme=seme)
                add.save()
                return render(request, 'add_student.html', {'semester_list': semester_list, 'dept_list': dept_list, 'dep_noti': dep_noti})

    return render(request, 'add_student.html', {'semester_list': semester_list, 'dept_list': dept_list})


def StDelete(request, p):
    student_list = add_student.objects.all()
    print(p)
    student = student_list.filter(s_id=p)
    student.delete()
    return redirect("student_list")


def student_list(request):
    student_list = add_student.objects.all()
    if request.method == "POST":
        #sem = request.GET.get('sem')
        dept = request.POST['dep']
        student_list = student_list.filter(dep=dept)
        print(dept)
        return render(request, "student_list.html", {'student_list': student_list})
    student_list = add_student.objects.all()
    return render(request, "student_list.html", {'student_list': student_list})


def teacher_list(request):
    teacher_list = add_teachers.objects.all()
    return render(request, "teacher_list.html", {'teacher_list': teacher_list})


def course_list(request):
    course_list = add_course.objects.all()
    if request.method == "POST":
        #sem = request.GET.get('sem')
        courseCode = request.POST['courseCode']
        course_list = course_list.filter(courseCode=courseCode)

        print(dept)
        return render(request, "course_list.html", {'course_list': course_list})
    return render(request, "course_list.html", {'course_list': course_list})


def department(request):
    dept_list = dept.objects.all()
    if request.method == "POST":
        dept_name = request.POST["dept_name"]
        dep_title = request.POST["dep_title"]
        dept_cradit = request.POST["dept_cradit"]
        if dept_list.filter(dept_name=dept_name):
            dep_noti = 0
            return render(request, "department.html", {'dept_list': dept_list, 'dep_noti': dep_noti, 'dept_name': dept_name})
        else:
            dep_noti = 1
            adddept = dept(dept_name=dept_name,
            dept_cradit=dept_cradit, dep_title=dep_title)
            adddept.save()
            return render(request, "department.html", {'dept_list': dept_list, 'dep_noti': dep_noti, 'dept_name': dept_name})
    dep_noti = ""

    return render(request, "department.html", {'dept_list': dept_list, 'dep_noti': dep_noti})


def semesters(request):
    seme=semester.objects.all()

    if request.method=="POST":
        name=request.POST['name']
        year=request.POST['year']
        semestername=name+year
        if(seme.filter(semester=semestername)):
            seme_noti=0
            return render(request, "semester.html",{'seme_noti':seme_noti,'seme':seme})
        else:
            addseme=semester(semester=semestername)
            addseme.save()
            seme_noti=1
            return render(request, "semester.html",{'seme_noti':seme_noti,'seme':seme})

    seme=semester.objects.all()

    return render(request, "semester.html",{'seme':seme})

def deletesemester(request, pk):

    seme = semester.objects.all()
    copomaping2 = seme.filter(id=pk)
    copomaping2.delete()

    return redirect("semesters")



def course_outcomes(request):
    dept_list = dept.objects.all()

    return render(request, "course_outcomes.html", {'dept_list': dept_list})


def program_outcomes(request):
    dept_list = dept.objects.all()

    return render(request, "pos.html", {'dept_list': dept_list})


def course_outcomes2(request, depname):
    cos_list = cos.objects.all()
    co_list = cos_list.filter(co_depname=depname)

    pos_list = pos.objects.all()
    po_list = pos_list.filter(po_depname=depname)

    if request.method == "POST":
        co_name = request.POST["co_name"]
        co_descriptions = request.POST["co_descriptions"]
        co_depname = depname
        
        if co_list.filter(co_name=co_name):
            cp_noti = 0
            return render(request, "course_outcomes2.html", {'co_list': co_list, 'cp_noti': cp_noti, 'co_name': co_name, 'depname': depname, "po_list": po_list})
        else:
            cp_noti = 1
            addco = cos(co_name=co_name, co_descriptions=co_descriptions,
                        co_depname=co_depname)
            addco.save()
            return render(request, "course_outcomes2.html", {'co_list': co_list, 'cp_noti': cp_noti, 'co_name': co_name, 'depname': depname, "po_list": po_list})
    cp_noti = ""

    return render(request, "course_outcomes2.html", {'co_list': co_list, 'depname': depname, 'po_list': po_list, "po_list": po_list})


def codelete(request,depname,pk):
    cos_list = cos.objects.all()
    co_list = cos_list.filter(co_depname=depname)
    co_list1 = co_list.filter(id=pk)
    co_list1.delete()
    
    return redirect('course_outcomes2',depname)






def program_outcomes2(request, depname):
    pos_list = pos.objects.all()
    po_list = pos_list.filter(po_depname=depname)
    if request.method == "POST":
        po_name = request.POST["po_name"]
        po_descriptions = request.POST["po_descriptions"]
        po_depname = depname
        if po_list.filter(po_name=po_name):
            cp_noti = 0
            return render(request, "pos2.html", {'po_list': po_list, 'cp_noti': cp_noti, 'po_name': po_name, 'depname': depname})
        else:
            cp_noti = 1
            addco = pos(po_name=po_name,
                        po_descriptions=po_descriptions, po_depname=po_depname)
            addco.save()
            return render(request, "pos2.html", {'po_list': po_list, 'cp_noti': cp_noti, 'po_name': po_name, 'depname': depname})
    cp_noti = ""

    return render(request, "pos2.html", {'po_list': po_list, 'depname': depname})


def co_poMapping(request):

    dept_list = dept.objects.all()

    return render(request, "co_poMapping.html", {'dept_list': dept_list})


def co_poMapping2(request, depname):
    pos_list = pos.objects.all()
    cos_list = cos.objects.all()
    add_course1 = add_course.objects.all()
    add_course2 = add_course1.filter(depname=depname)
    copomaping1 = copomaping.objects.all()
    if request.method == "POST":
        #sem = request.GET.get('sem')
        courseCode = request.POST['courseCode']
        add_course2 = add_course2.filter( courseCode =  courseCode )
        print( dept )
        return render( request , "co_poMapping2.html", {'add_course2': add_course2 , 'depname': depname, 'copomaping1': copomaping1 })
    add_course1 = add_course.objects.all()
    return render(request, "co_poMapping2.html", { 'add_course2': add_course2, 'depname': depname, 'copomaping1': copomaping1 })


def co_poMapping3(request, cc, depname):

    map_noti = ''
    pos_list = pos.objects.all()
    po_list = pos_list.filter( po_depname = depname )
    add_course1 = add_course.objects.all()
    add_course2 = add_course1.filter( courseCode = cc )
    cos_list = cos.objects.all()
    cos_list2 = cos_list.filter(co_depname=depname)
    copomaping1 = copomaping.objects.all()
    copomaping2 = copomaping1.filter(copomapingCc=cc)
    courseCos1=courseCos.objects.all()
    course_assesments_mark1=course_assesments_mark.objects.all()
    course_assesments_mark2=course_assesments_mark1.filter(course_assid=cc)
    
    coursePos1=coursePos.objects.all()
    
    coursePos2=coursePos1.filter(coursePos_id=cc)


    if request.method == "POST":
        

        copomapingCo = request.POST["copomapingCo"]

        copomapingpo=request.POST["copomapingpo"]

        if(copomaping2.filter(copomapingCo=copomapingCo)):

            copomaping3=copomaping2.filter(copomapingCo=copomapingCo)
                                           
            if(copomaping3.filter(copomapingpo=copomapingpo)):
                map_noti = 1
            else:
                courseCosname=copomapingCo
                courseCos2=courseCos1.filter(courseCos_id=cc)
                courseCos3=courseCos2.filter(courseCosname=copomapingCo)
                
                
                if(courseCos2.filter(courseCosname=copomapingCo)):
                    print(copomapingpo)
                    if(coursePos2.filter(coursePosname=copomapingpo)):
                        print(copomapingpo)
                    else:
                        addcoursePos= coursePos(coursePos_id=cc,coursePosname=copomapingpo)
                        addcoursePos.save()
                else:

                    addcourseCos= courseCos(courseCos_id=cc,courseCosname=courseCosname)
                    addcourseCos.save()

                    for co in courseCos2:
                        course_classid=cc
                        course_asses_name=cc.course_ass_name
                        course_co_name= co.courseCosname
                        course_asses_point=0.0
                        addco=course_lms_wieght(course_classid=course_classid,course_asses_name=course_asses_name,course_co_name=course_co_name,course_asses_point=course_asses_point)
                        addco.save()

                    if(coursePos2.filter(coursePosname=copomapingpo)):
                        print(copomapingpo)
                    else:
                        print(copomapingpo)
                        addcoursePos= coursePos(coursePos_id=cc,coursePosname=copomapingpo)
                        addcoursePos.save()
            
                map_noti = 0
                addcopomap = copomaping(copomapingCc=cc, copomapingCo=copomapingCo, copomapingpo=copomapingpo)
                addcopomap.save()

                
                

                return render(request, "co_poMapping3.html", {'add_course2': add_course2,'po_list': po_list, 'cos_list2': cos_list2, "copomaping2": copomaping2, 'map_noti': map_noti, 'depname': depname, 'cc': cc})
            
        else:
            
            courseCosname=copomapingCo
            courseCos2=courseCos1.filter(courseCos_id=cc)
            courseCos3=courseCos2.filter(courseCosname=courseCosname).count()
            

            if(courseCos2.filter(courseCosname=copomapingCo)):
                print(courseCos3)
            else:
                addcourseCos= courseCos(courseCos_id=cc,courseCosname=courseCosname)
                addcourseCos.save()

            if(coursePos2.filter(coursePosname=copomapingpo)):
                print(copomapingpo)
            else:
                print(copomapingpo)
                addcoursePos= coursePos(coursePos_id=cc,coursePosname=copomapingpo)
                addcoursePos.save()

            map_noti = 0
            addcopomap = copomaping(
                        copomapingCc=cc, copomapingCo=copomapingCo, copomapingpo=copomapingpo)
            addcopomap.save()
            return render(request, "co_poMapping3.html", {'add_course2': add_course2,'po_list': po_list, 'cos_list2': cos_list2, "copomaping2": copomaping2, 'map_noti': map_noti, 'depname': depname, 'cc': cc})
    return render(request, "co_poMapping3.html", {'add_course2': add_course2,'po_list': po_list, 'cos_list2': cos_list2, "copomaping2": copomaping2, 'map_noti': map_noti, 'depname': depname, 'cc': cc})


def deleteco_poMapping(request, depname, cc, pk):

    copomaping1 = copomaping.objects.all()
    copomaping2 = copomaping1.filter(id=pk)
    courseCos1=courseCos.objects.all()
    coursePos1=coursePos.objects.all()

    for copo in copomaping2:
        copomapingCo=copo.copomapingCo
        copomapingPo=copo.copomapingpo

    copomaping3=copomaping1.filter(copomapingCc=cc) #course code

    copomaping4=copomaping3.filter(copomapingCo=copomapingCo).count()

    copomaping5=copomaping3.filter(copomapingpo=copomapingPo).count()

    print(copomaping4)

    if(copomaping4==1):
        courseCos2=courseCos1.filter(courseCos_id=cc)
        courseCos3=courseCos2.filter(courseCosname=copomapingCo)
        courseCos3.delete()
    
    if(copomaping5==1):
        coursePos2=coursePos1.filter(coursePos_id=cc)
        coursePos3=coursePos2.filter(coursePosname=copomapingPo)
        coursePos3.delete()

    copomaping2.delete()
    return redirect("co_poMapping3", depname, cc)


# Faiza


def add_courses(request):
    add_courses_noti = 0
    add_course1 = add_course.objects.all()
    dept_list = dept.objects.all()
    if request.method == "POST":
        courseName = request.POST['courseName']
        courseCode = request.POST['courseCode']
        depname = request.POST["depname"]
        credit = request.POST['credit']
        if (add_course1.filter(courseCode=courseCode)):
            add_courses_noti = 2
            return render(request, 'add_course.html', {'dept_list': dept_list, 'add_courses_noti': add_courses_noti, 'courseCode': courseCode})
        elif (add_course1.filter(courseName=courseName)):
            add_courses_noti = 3
            return render(request, 'add_course.html', {'dept_list': dept_list, 'add_courses_noti': add_courses_noti, 'courseName': courseName})
        else:
            add_courses_noti = 1
            c_add = add_course(
                courseName=courseName, courseCode=courseCode, credit=credit, depname=depname)
            c_add.save()
            return render(request, 'add_course.html', {'dept_list': dept_list, 'add_courses_noti': add_courses_noti, 'courseCode': courseCode})
    return render(request, 'add_course.html', {'dept_list': dept_list, 'add_courses_noti': add_courses_noti})


def add_teacher(request):
    dept_list = dept.objects.all()
    if request.method == "POST":
        tfirstName = request.POST['tfirstName']
        tlastName = request.POST['tlastName']
        t_id = request.POST['t_id']
        tgender = request.POST['tgender']
        tp_email = request.POST['tp_email']
        tphone = request.POST['tphone']
        tdep = request.POST['tdep']
        tCode = request.POST['tCode']
        t_add = add_teachers(tfirstName=tfirstName, tlastName=tlastName, t_id=t_id,
                             tgender=tgender, tp_email=tp_email, tphone=tphone, tdep=tdep, tCode=tCode)
        t_add.save()
    return render(request, 'add_teacher.html', {'dept_list': dept_list})


def logoutuser(request):
    logout(request)
    messages.success(request, 'Successfully logout!')
    return redirect("signup")



def weightx(request,x):
    cos_list=cos.objects.all()
    course_list=add_course.objects.all()
    courseCos1=courseCos.objects.all()
    courseCos2=courseCos1.filter(courseCos_id=x)
    
    course_assesments_mark1=course_assesments_mark.objects.all()
    course_assesments_mark2=course_assesments_mark1.filter(course_assid=x)
    course_wieght_number1=course_wieght_number.objects.all()
    course_wieght_number2=course_wieght_number1.filter(course_class_id=x)

    course_lms_wieght1=course_lms_wieght.objects.all()
    course_lms_wieght2=course_lms_wieght1.filter(course_classid=x)

    weightx=course_weight_ass.objects.all()
    weightx1=weightx.filter(wieghtClassid=x)
    
    
    class4=course_list.filter(courseCode=x)

    for class5 in class4:
        class6=class5.depname

    co_lis=cos_list.filter(co_depname=class6)

    others_course_assesments_mark1=others_course_assesments_mark.objects.all()
    others_course_assesments_mark2=others_course_assesments_mark1.filter(others_course_assid=x)

    
    if request.method=="POST":
        xx=0
        for ass in course_assesments_mark2:
                x1=0


                for co in courseCos2:
                    co1=co.courseCosname
                    p=ass.course_ass_name+co.courseCosname
                    p=request.POST[p]
                    #print(p)
                    x1=float(x1)+float(p)
                    student=course_lms_wieght2.filter(course_asses_name=ass.course_ass_name)
                    student1=student.filter(course_co_name=co1)
                    for i in student1:
                        member = course_lms_wieght.objects.get(id=i.id)
                        member.course_asses_point = p
                        
                

                    #print("x1",x1,ass.ass_name)
                

                others_course_assesments_mark3=others_course_assesments_mark2.filter(others_course_ass_name=ass.course_ass_name)
                for o in others_course_assesments_mark3:
                    p2=ass.course_ass_name+"Others"
                    p2=request.POST[p2]
                    print(p2)
                    others=others_course_assesments_mark.objects.get(id=o.id)
                    others.others_course_ass_point=p2
                    #others.save()

                    xx=float(xx)+float(others.others_course_ass_point)

                



                total3=course_wieght_number2.filter(course_Exam_name=ass.course_ass_name)
                #print(total3)
                for t in total3:
                
                    r=t.course_Exam_name
                    course_ratio=request.POST[r]
                    total5=course_wieght_number.objects.get(id=t.id)
                    total5.course_taken=x1
                    total5.course_ratio=course_ratio
                    total5.course_wieght=float(course_ratio)*float(x1)
                    #print("xx1",xx)
                    xx=float(xx)+float(total5.course_wieght)
                    #print(xx)
                    
                

        ############################################
        print(xx)
        if(xx<=100):
            xx=0
            for ass in course_assesments_mark2:
                x1=0
                for co in courseCos2:

                    co1=co.courseCosname
                    p=ass.course_ass_name+co.courseCosname
                    p=request.POST[p]

                    #print(p)
                    x1=float(x1)+float(p)
                    student=course_lms_wieght2.filter(course_asses_name=ass.course_ass_name)
                    student1=student.filter(course_co_name=co1)
                    for i in student1:
                        member = course_lms_wieght.objects.get(id=i.id)
                        member.course_asses_point = p
                        member.save()
                

                    #print("x1",x1,ass.ass_name)
                others_course_assesments_mark3=others_course_assesments_mark2.filter(others_course_ass_name=ass.course_ass_name)
                

                total3=course_wieght_number2.filter(course_Exam_name=ass.course_ass_name)
                #print(total3)
                for t in total3:
                
                    r=t.course_Exam_name
                    course_ratio=request.POST[r]
                    total5=course_wieght_number.objects.get(id=t.id)
                    
                    total5.course_taken=x1
                    total5.course_ratio=course_ratio

                    p2=ass.course_ass_name+"Others"
                    p2=request.POST[p2]
                    print(p2)

                    total5.course_taken=float(x1)+float(p2)

                    for o in others_course_assesments_mark3:
                        
                        others=others_course_assesments_mark.objects.get(id=o.id)
                        others.others_course_ass_point=p2
                        others1=others.others_course_ass_point
                        
                        x1=float(x1)+float(others1)

                        others.save()

                    total5.course_wieght=float(course_ratio)*float(x1)
                    #print("xx1",xx)
                    xx=float(xx)+float(total5.course_wieght)
                    #print(xx)
                    total5.save()

            #print(x1)
            
            weight_ass3=course_weight_ass.objects.all()
            if weight_ass3.filter(wieghtClassid=x):

                for weight_ass4 in weight_ass3:
                    weight_ass3=course_weight_ass.objects.get(id=weight_ass4.id)
                    weight_ass3.totalweight=xx
                    weight_ass3.save()

            else:

                wieghtClassid=x
                totalweight=xx
                addw=course_weight_ass(wieghtClassid=wieghtClassid,totalweight=totalweight)
                addw.save()
            noti=1
        else:
            noti=2

        total2=course_wieght_number.objects.all()

        weightx=course_weight_ass.objects.all()
        weightx1=weightx.filter(wieghtClassid=x)

        total=total2.filter(course_class_id=x)
        weightx1=weightx.filter(wieghtClassid=x)

        lms_wieght1=course_lms_wieght.objects.all()
        lms_wieght2=lms_wieght1.filter(course_classid=x)

        classco1=courseCos.objects.all()
        classco2=classco1.filter(courseCos_id=x)

        for co1 in courseCos2:
            lms_wieght3=lms_wieght2.filter(course_co_name=co1.courseCosname)
            comark=0
            for lms_wieght4 in lms_wieght3:
                comark=float(lms_wieght4.course_asses_point)+float(comark)
            classco11=courseCos.objects.get(id=co1.id)
            classco11.courseCosmark=comark
            classco11.save()
        

        courseCos2=courseCos1.filter(courseCos_id=x)
        
                 













        return render(request ,'wieghtx.html',{"others_course_assesments_mark2":others_course_assesments_mark2,'x':x ,"noti":noti,"weightx1":weightx1,"course_lms_wieght2":course_lms_wieght2,"course_wieght_number2":course_wieght_number2,"courseCos2":courseCos2,'course_assesments_mark2':course_assesments_mark2})
    noti=""

    return render(request ,'wieghtx.html',{"others_course_assesments_mark2":others_course_assesments_mark2,'x':x ,"noti":noti,"course_lms_wieght2":course_lms_wieght2,"course_wieght_number2":course_wieght_number2,"courseCos2":courseCos2,'course_assesments_mark2':course_assesments_mark2})


def Deleteadd(request,x,pk,ex):

    course_assesments_mark1=course_assesments_mark.objects.all()
    course_assesments_mark2=course_assesments_mark1.filter(id=pk)
    course_assesments_mark2.delete()


    course_wieght_number1=course_wieght_number.objects.all()
    course_wieght_number2=course_wieght_number1.filter(course_class_id=x)
    course_wieght_number3=course_wieght_number2.filter(course_Exam_name=ex)
    course_wieght_number3.delete()

    course_lms_wieght1=course_lms_wieght.objects.all()
    course_lms_wieght2=course_lms_wieght1.filter(course_classid=x)
    course_lms_wieght3=course_lms_wieght2.filter(course_asses_name=ex)
    course_lms_wieght3.delete()

    others_course_assesments_mark1=others_course_assesments_mark.objects.all()
    others_course_assesments_mark2=others_course_assesments_mark1.filter(others_course_assid=x)
    others_course_assesments_mark3=others_course_assesments_mark2.filter(others_course_ass_name=ex)
    others_course_assesments_mark3.delete()

    return redirect ('upCourse',x)




def upCourse(request,x):

    course_list=add_course.objects.all()
    course_list1=course_list.filter(courseCode=x)

    for c1 in course_list1:
        dep=c1.depname


    course_assesments_mark1=course_assesments_mark.objects.all()
    if request.method=="POST":
        course_assid=x
        course_ass_name=request.POST["course_ass_name"]
        course_ass_point=0
        course_assesments_mark2=course_assesments_mark1.filter(course_assid=x)

        if(course_assesments_mark1.filter(course_assid=x)):
            course_assesments_noti=0
            if(course_assesments_mark2.filter(course_ass_name=course_ass_name)):
                course_assesments_noti=0

            else:
                add=course_assesments_mark(course_assid=course_assid,course_ass_name=course_ass_name,course_ass_point=course_ass_point)
                add.save()

                others_course_assid=x
                others_course_ass_name= course_ass_name
                others_course_ass_point=0.0
                others_course_others_name="Others"
                
                addothers=others_course_assesments_mark(others_course_assid=others_course_assid,others_course_ass_name=others_course_ass_name,others_course_others_name=others_course_others_name,others_course_ass_point=others_course_ass_point)
                addothers.save()

                course_class_id=x
                course_Exam_name=course_ass_name
                course_wieght=0.0
                course_taken=0.0
                course_ratio=0.0
                addweight=course_wieght_number(course_class_id=course_class_id,course_Exam_name=course_Exam_name,course_wieght=course_wieght,course_taken=course_taken,course_ratio=course_ratio)
                addweight.save()

                courseCos1=courseCos.objects.all()
                courseCos2=courseCos1.filter(courseCos_id=x)

                for co in courseCos2:
                    course_classid=x
                    course_asses_name=course_ass_name
                    course_co_name= co.courseCosname
                    course_asses_point=0.0
                    addco=course_lms_wieght(course_classid=course_classid,course_asses_name=course_asses_name,course_co_name=course_co_name,course_asses_point=course_asses_point)
                    addco.save()

        else:
                add=course_assesments_mark(course_assid=course_assid,course_ass_name=course_ass_name,course_ass_point=course_ass_point)
                add.save()

                others_course_assid=x
                others_course_ass_name= course_ass_name
                others_course_ass_point=0.0
                others_course_others_name="Others"
                
                addothers=others_course_assesments_mark(others_course_assid=others_course_assid,others_course_ass_name=others_course_ass_name,others_course_others_name=others_course_others_name,others_course_ass_point=others_course_ass_point)
                addothers.save()

                course_class_id=x
                course_Exam_name=course_ass_name
                course_wieght=0.0
                course_taken=0.0
                course_ratio=0.0
                addweight=course_wieght_number(course_class_id=course_class_id,course_Exam_name=course_Exam_name,course_wieght=course_wieght,course_taken=course_taken,course_ratio=course_ratio)
                addweight.save()

                courseCos1=courseCos.objects.all()
                courseCos2=courseCos1.filter(courseCos_id=x)

                for co in courseCos2:
                    course_classid=x
                    course_asses_name=course_ass_name
                    course_co_name= co.courseCosname
                    course_asses_point=0.0
                    addco=course_lms_wieght(course_classid=course_classid,course_asses_name=course_asses_name,course_co_name=course_co_name,course_asses_point=course_asses_point)
                    addco.save()

    course_assesments_mark2=course_assesments_mark1.filter(course_assid=x)
    return render(request, 'upCourse.html',{"dep":dep,"x":x,'course_assesments_mark2':course_assesments_mark2})



def roule(request):
    p="0"
    roule1=rouleW.objects.all()

    for roule4 in roule1:
        p=roule4.roulesPoint



    if request.method=="POST":

        roulesname="weight"
        roulesPoint=request.POST["roulesPoint"]
        
        if (rouleW.objects.all()):
            p=roulesPoint
            for roule2 in roule1:
                r1=rouleW.objects.get(id=roule2.id)
                r1.roulesPoint=roulesPoint
                r1.save()
        else:
            p=roulesPoint
            addroule=rouleW(roulesname=roulesname,roulesPoint=roulesPoint)
            addroule.save()

    print(p)

    
    return render(request,'roule.html',{"p":p})


def feed(request):

    teachersFeadback1=teachersFeadback.objects.all()

    if request.method=="POST":
        courseCode=request.POST['courseCode']
        teachersFeadback1=teachersFeadback1.filter(teachersFeadbackcourse=courseCode)





    return render(request,'feedback.html',{'teachersFeadback1':teachersFeadback1})


def copo(request,depname,cc):
    
    return redirect('co_poMapping3',depname,cc)