from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from .models import rouleW,usersemester,gread,AssMark,assesments_mark,lms_wieght,wieght_number, wieght_total,weight_ass      
from django.contrib import messages
from result.models import teachersFeadback,others_assesment_mark,others_assesments_mark,others_course_assesments_mark,classco,courseCos,greading,duptclsRoom, clsStudent,assesment_mark,copomaping
from result.views import pOAttainment,classcopomaping,classPo,coAttainment,semester,add_teachers, clsStudent ,clsRoom, add_course,cos,add_student
from django.urls import reverse
from django.db import connections
from django.http import JsonResponse

# Create your views here.



def teachercourse(request):
    newclass_list=duptclsRoom.objects.all()
    for newcls in newclass_list:

        newcls.delete()

    
    email=request.session['name']
    teacher_list=add_teachers.objects.all()

    teach=teacher_list.filter(tp_email=email)

    for tech in teach:
        th=tech.tCode

    clsRoom_list=clsRoom.objects.all()
    usersemester1=usersemester.objects.all()
    usersemesterx=usersemester1.filter(user_id=th)
    teacher=clsRoom_list.filter(instructor=th)
    semester1=semester.objects.all()
    cn=add_course.objects.all()
    

    
    return render(request,"course.html",{'teacher':teacher,'cn':cn , 'semester1':semester1,'usersemesterx':usersemesterx,'th':th })


def teacherHome(request):


    return render(request ,'teacherHome.html')


def assesment(request,assName,x):

    roule1=rouleW.objects.all()

    for roule4 in roule1:

        p=roule4.roulesPoint

    print(assName)
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

    others_assesment_mark1=others_assesment_mark.objects.all()
    others_assesment_mark2=others_assesment_mark1.filter(others_classId=x)
    others_assesment_mark3=others_assesment_mark2.filter(others_assesmentName=assName)

    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=assName)
    


    return render(request ,'assesment.html',{"p":p,"others_assesments_mark3":others_assesments_mark3,"others_assesment_mark3":others_assesment_mark3,'classco2':classco2,"cos_list2":cos_list2,'studentName':studentName,'x':x, 'assName':assName, 'exam':exam, 'class3':class3,'class4':class4, 'instructor':instructor,"firstName":firstName,"lastName":lastName,'courseName':courseName,'credit':credit,'classSemester':classSemester,'courseCos2':courseCos2,'weight3':weight3,"student1":student1,'cos_list2':cos_list2,'ass2':ass2})





def teacherresult(request,x):

    roule1=rouleW.objects.all()

    for roule4 in roule1:
        p=roule4.roulesPoint



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

    classPo1= classPo.objects.all()
    classPo2=classPo1.filter(classPoId=x)

    greading1=greading.objects.all()


    assesment_mark1=assesment_mark.objects.all()
    assesment_mark2=assesment_mark1.filter(classId=x)

    clsstudent1=clsStudent.objects.all()
    avg=clsstudent1.filter(classCod=x).count()
    


    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)

    coAttainment1=coAttainment.objects.all()
    coAttainment2=coAttainment1.filter(coAttainmentId=x)

    pOAttainment1=pOAttainment.objects.all()
    pOAttainment2=pOAttainment1.filter(pOAttainmentId=x)

    for coAttainment3 in coAttainment2:
        att = "0"
        att2="0"
        Attainment="0"
        co = coAttainment3.coAttainmentCosname
        #print(co)
        assesment_mark4 = assesment_mark2.filter(coName=co)

        for assesment_mark5 in assesment_mark4:
            mark=assesment_mark5.mark
            att= float(att)+ float(mark)

        classco3=classco2.filter(classCosname=co)

        #print(att)
        #print(avg)

        for classco4 in classco3:
            att2=classco4.classCosmark

        
        if(float(avg)!=0):
            att=(float(att)/ float(avg))

        coAttainment3=coAttainment2.filter(coAttainmentCosname=co)

        #print(att2)

        if(float(att2)!=0 ):
            Attainment=(float(att)/float(att2))*100


        for coAttainment4 in coAttainment3:
            coAttainment5=coAttainment.objects.get(id=coAttainment4.id)
            coAttainment5.coAttainmentCosmark=att
            coAttainment5.coAttainmentAttainment=Attainment
            coAttainment5.save()


        #print(Attainment)

    
    classcopomaping1=classcopomaping.objects.all()
    classcopomaping2=classcopomaping1.filter(copomapingCc= x)

    classPo1=classPo.objects.all()

    classPo2=classPo1.filter(classPoId=x)

    

    for po in classPo2:
        at=0
        po1=po.classPosname
        classcopomaping3=classcopomaping2.filter(copomapingpo=po1)
        for co in classcopomaping3:
            co1=co.copomapingCo
            assesment_mark4 = assesment_mark2.filter(coName=co1)
            po2=po.classPosmark
            
            for assesment_mark5 in assesment_mark4:
                mark=assesment_mark5.mark
                at= float(at)+ float(mark)

        print(po2)
        print(at)

        

        classPo3=classPo2.filter(classPosname=po1)

        for classPo4 in classPo3:
            att2=classPo4.classPosmark



        if(float(avg)!=0):
            at=(float(at)/ float(avg))

        if(float(att2)!=0 ):
            Attainment=(float(at)/float(att2))*100

        
        
        print(Attainment)

        pOAttainment3=pOAttainment2.filter(pOAttainmentCosname=po1)
        print(pOAttainment3)
        for poa in pOAttainment3:
            attain=pOAttainment.objects.get(id=poa.id)
            attain.pOAttainmentCosmark=at
            attain.pOAttainmentAttainment=Attainment
            attain.save()

    pOAttainment2=pOAttainment1.filter(pOAttainmentId=x)




    for g in gread2:
        m=0
        for a in AssMark2:
            if (a.markS_id==g.greadS_id):
                m=float(m)+float(a.MarkAss)
        studentgread=gread.objects.get(id=g.id)
       
        studentgread.greadtotalmark=m

        for g1 in greading1:
            if( float(m) >= float(g1.firstMark) and float(m) < float(g1.secMark) ):
                
                studentgread.greadLetter=g1.greadLetter
        
        studentgread.save()

    greading1=greading.objects.all()
    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)

    coAttainment1=coAttainment.objects.all()
    coAttainment2=coAttainment1.filter(coAttainmentId=x)
    
    #print(exam)
    if request.method=="POST":
        assid=x
        asss_name=request.POST["ass_name"]
        ass_point=0
        wieght_total1=wieght_total.objects.all()
        if exam.filter(ass_name = asss_name):
            noti=0
        else:
            classid=x
            asses_name=asss_name
            asses_point=0

            for co in classco2:
                cos_name=co.classCosname
                
                addco=lms_wieght(classid=classid,asses_name=asses_name, asses_point=asses_point,co_name=cos_name)
                addco.save()
                
                totalClassid=x
                totalAsses_name=asses_name
                totalCo_name=cos_name
                totalpoint=0

                addTotal=wieght_total(totalClassid=totalClassid,totalAsses_name=totalAsses_name,totalCo_name=totalCo_name,totalpoint=totalpoint)
                addTotal.save()

            dep1=clsRoom.objects.all()
            dep2=dep1.filter(classCode=x)
            for dep3 in dep2:
                courseCode=dep3.courseCod
                dep4=add_course.objects.all()
                dep5=dep4.filter(courseCode=courseCode)
                for dep6 in dep5:
                    dep=dep6.depname
            cos_list= cos.objects.all() 
            cos_list1=cos_list.filter(co_depname=dep)

            courseCos1=courseCos.objects.all()
            courseCos2=courseCos1.filter(courseCos_id=class3)

            class_id=x
            Exam_name=asss_name
            wieght=ass_point
            taken=0
            ratio=0
            
            addw=wieght_number(class_id=class_id,Exam_name=Exam_name, wieght=wieght,taken=taken,ratio=ratio)
            addw.save()
            
            noti=1
            addass=assesments_mark(assid=assid,ass_name=asss_name,ass_point=ass_point)
            addass.save()
            gread1=gread.objects.all()
            gread2=gread1.filter(greadClassId=x)

            others_assid=x
            others_ass_name=Exam_name
            others_others_name='Others'
            others_ass_point=0
            addothers_assesments_mark=others_assesments_mark(others_assid=others_assid,others_ass_name=others_ass_name,others_others_name=others_others_name,others_ass_point=others_ass_point )
            addothers_assesments_mark.save()

            for s1 in student1:
                #for ass2 in ass1:
                    assesmentName=Exam_name
                    for co in classco2:
                        classId=x
                        studentId=s1.stdid
                        assesmentName=assesmentName
                        coName=co.classCosname
                        mark=0
                        addassesment_mark=assesment_mark(classId=classId,studentId=studentId,assesmentName=assesmentName,coName=coName,mark=mark)
                        addassesment_mark.save()

                    
                    others_classId=x
                    others_studentId=s1.stdid
                    others_assesmentName=assesmentName
                    others_coName='Others'
                    others_mark=0
                    addothers_assesment_mark=others_assesment_mark(others_classId=others_classId,others_studentId=others_studentId,others_assesmentName=others_assesmentName,others_coName=others_coName,others_mark=others_mark )
                    addothers_assesment_mark.save()

                    markS_id=s1.stdid
                    markClassId=x
                    markAssName=assesmentName
                    MarkAss=0
                    addAssMark=AssMark(markS_id=markS_id,markClassId=markClassId,markAssName=markAssName,MarkAss=MarkAss)
                    addAssMark.save()

            
            gread1=gread.objects.all()
            gread2=gread1.filter(greadClassId=x)
            AssMark2=AssMark1.filter(markClassId=x)

            classcopomaping1=classcopomaping.objects.all()
            classcopomaping2=classcopomaping1.filter(copomapingCc=x)

            classPo1=classPo.objects.all()
            classPo2=classPo1.filter(classPoId=x)
            
            for po in classPo2:
                po1=po.classPosname
                classcopomaping3=classcopomaping2.filter(copomapingpo=po1)
                com=0
                for classcopomaping4 in classcopomaping3:
                    co=classcopomaping4.copomapingCo
                    classco3=classco2.filter(classCosname=co)
                    for co4 in classco3:
                        com=float(com)+co4.classCosmark
                
                pom=classPo.objects.get(id=po.id)
                pom.classPosmark=com
                pom.save()
            
            return render(request ,'teacherResult.html',{"pOAttainment2":pOAttainment2, "classPo2":classPo2, "coAttainment2":coAttainment2,  "p":p,'classco2':classco2,'gread2':gread2,'courseName':courseName,'studentName':studentName,'AssMark2':AssMark2,'mark1':mark1,'totalweight':totalweight,'weight1':weight1,'student1':student1,'x':x,'exam':exam,'noti':noti, 'class3':class3, 'sec':sec,'credit':credit,
    "classSemester":classSemester,'wieght_number2':wieght_number2})
    gread1=gread.objects.all()
    gread2=gread1.filter(greadClassId=x)
    return render(request ,'teacherResult.html',{"pOAttainment2":pOAttainment2, "classPo2":classPo2, "coAttainment2":coAttainment2, "p":p,'classco2':classco2,'gread2':gread2,'studentName':studentName,'AssMark2':AssMark2,'mark1':mark1,'totalweight':totalweight,'weight1':weight1,'student1':student1,'x':x,'exam':exam,'noti':noti, 'class3':class3, 'sec':sec,
    'firstName':firstName,'lastName':lastName,'courseName':courseName,'credit':credit,
    "classSemester":classSemester,'wieght_number2':wieght_number2})

def deleteMark(request,x,assName):

    assesment=assesments_mark.objects.all()
    assesment2=assesment.filter(assid=x)
    assesment3=assesment2.filter(ass_name=assName)
    assesment3.delete()

    weight1=lms_wieght.objects.all()
    weight2=weight1.filter(classid=x)
    weight3=weight2.filter(asses_name=assName)
    weight3.delete()

    wieghtNumber=wieght_number.objects.all()
    wieghtNumber2=wieghtNumber.filter(class_id=x)
    wieghtNumber3=wieghtNumber2.filter(Exam_name=assName)
    wieghtNumber3.delete()

    mark=assesment_mark.objects.all()
    mark2=mark.filter(classId=x)
    mark3=mark2.filter(assesmentName=assName)
    mark3.delete()

    AssMark1=AssMark.objects.all()
    AssMark2=AssMark1.filter(markClassId=x)
    AssMark3=AssMark2.filter(markAssName=assName)
    AssMark3.delete()

    others_assesment_mark1=others_assesment_mark.objects.all()
    others_assesment_mark2=others_assesment_mark1.filter(others_classId=x)
    others_assesment_mark3=others_assesment_mark2.filter(others_assesmentName=assName)
    others_assesment_mark3.delete()

    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=assName)
    others_assesments_mark3.delete()


    return redirect(teacherresult,x)


def updatresult(request,x,s_id,assName):

    others_assesment_mark1=others_assesment_mark.objects.all()
    others_assesment_mark2=others_assesment_mark1.filter(others_classId=x)
    others_assesment_mark3=others_assesment_mark2.filter(others_assesmentName=assName)
    others_assesment_mark4=others_assesment_mark3.filter(others_studentId=s_id)
    others_assesment_mark5=others_assesment_mark4.filter(others_coName="Others")
 
    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=assName)


    for a1 in others_assesments_mark3:
        others=a1.others_ass_point
    
    print(others)

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

    studentName=add_student.objects.all()

    course=add_course.objects.all()
    course2=course.filter(courseCode=class3)

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

    classco1=classco.objects.all()
    classco2=classco1.filter(classId=x)

    studentName=add_student.objects.all()
    AssMark1=AssMark.objects.all()
    ass=assesment_mark.objects.all()
    ass1=ass.filter(classId=classCode)
    ass2=ass1.filter(assesmentName=assName)
    ass3=ass2.filter(studentId=s_id)
    mark_noti=0
    xx=0

    AssMark11=AssMark.objects.all()
    AssMark22=AssMark11.filter(markClassId=x)

    gread11=gread.objects.all()
    gread22=gread11.filter(greadClassId=x)

    wieght_number1=wieght_number.objects.all()
    wieght_number2=wieght_number1.filter(class_id=x)
    wieght_number3=wieght_number2.filter(Exam_name=assName)
    
    courseCos1=courseCos.objects.all()
    courseCos2=courseCos1.filter(courseCos_id=class3)


    if request.method=="POST":

        a2=request.POST['Others']
        print(a2)

        for m in others_assesment_mark5:
            others1=others_assesment_mark.objects.get(id=m.id)

            if(  float(a2) <= float(others)):
                others1.others_mark=a2
                a3=a2
                print(others1.others_mark)
                others1.save()

            else:
                mark_noti=2
                return render(request, 'assupdate.html',{ "others_assesment_mark4":others_assesment_mark4, "others_assesments_mark3":others_assesments_mark3,"others_assesment_mark3":others_assesment_mark3,  'classco2':classco2,'ass3':ass3,'courseCos2':courseCos2,"mark_noti":mark_noti,'class3':class3,'class4':class4,"assName":assName,"studentName":studentName,'s_id':s_id,"cos_list2":cos_list2,'classSemester':classSemester,'weight3':weight3,"student1":student1,'ass2':ass2,'x':x})


        for co in cos_list2:

            

            for co1 in classco2:
                if(co.co_name==co1.classCosname):
                    num=assName+co.co_name
                    mark1=request.POST[num]
                    
                    yy=0
                    for i in ass3:
                        co1=i.coName
                        co2=assName+co1
                        if(num==co2): #compare with co points
                            sub=lms_wieght.objects.all()
                            sub2=sub.filter(classid=x)
                            sub3=sub2.filter(asses_name=assName)
                            sub4=sub3.filter(co_name=co1)
                            #print(co1)
                        
                            for i2 in sub4:
                                #print(mark1)
                                #print(i2.asses_point)
                                if (float(mark1)<=i2.asses_point):
                                    mark_noti=1
                                    member = assesment_mark.objects.get(id=i.id)
                                    
                                    member.mark=float(mark1)
                                    xx=float(xx)+float(member.mark)
                                    
                                    member.save()
                                elif(float(mark1)>i2.asses_point):
                                    mark_noti=2
                                    return render(request, 'assupdate.html',{ "others_assesment_mark4":others_assesment_mark4, "others_assesments_mark3":others_assesments_mark3,"others_assesment_mark3":others_assesment_mark3,  'classco2':classco2,'ass3':ass3,'courseCos2':courseCos2,"mark_noti":mark_noti,'class3':class3,'class4':class4,"assName":assName,"studentName":studentName,'s_id':s_id,"cos_list2":cos_list2,'classSemester':classSemester,'weight3':weight3,"student1":student1,'ass2':ass2,'x':x})
        AssMark2=AssMark1.filter(markClassId=x)
        AssMark3=AssMark2.filter(markS_id=s_id)
        AssMark4=AssMark3.filter(markAssName=assName)
        for a in AssMark4:
            AssMark5=AssMark.objects.get(id=a.id)  
            for wieght_number4 in wieght_number3: 
                MarkAss=float(xx)*float(wieght_number4.ratio)
                
            AssMark5.MarkAss=float(MarkAss)+(float(a2)*float(wieght_number4.ratio) )

            AssMark5.save()

        greading1=greading.objects.all()
        
        for g in gread22:
            m=0
            for a in AssMark22:
                if (a.markS_id==g.greadS_id):
                    m=float(m)+float(a.MarkAss)

            print(m)
            studentgread=gread.objects.get(id=g.id)
            studentgread.greadtotalmark=m
            for g1 in greading1:
                if( float(m) <= float(g1.firstMark) and float(m) > float(g1.secMark) ):
                    studentgread.greadLetter=g1.greadLetter
                    break
            studentgread.greadtotalmark=m
            studentgread.save()
        gread11=gread.objects.all()
        gread22=gread11.filter(greadClassId=x)
        return render(request ,'assesment.html',{"others_assesment_mark4":others_assesment_mark4, "others_assesments_mark3":others_assesments_mark3,"others_assesment_mark3":others_assesment_mark3, 'classco2':classco2,'courseCos2':courseCos2,'mark_noti':mark_noti,'studentName':studentName,'x':x, 'assName':assName, 'exam':exam, 'class3':class3,'class4':class4, 'instructor':instructor,"firstName":firstName,"lastName":lastName,'courseName':courseName,'credit':credit,'classSemester':classSemester,'cos_list2':cos_list2,'weight3':weight3,"student1":student1,'ass3':ass3,'ass2':ass2})
    gread11=gread.objects.all()
    gread22=gread11.filter(greadClassId=x)            
    return render(request, 'assupdate.html',{"others_assesment_mark4":others_assesment_mark4,"others_assesments_mark3":others_assesments_mark3,"others_assesment_mark3":others_assesment_mark3,'classco2':classco2,'ass3':ass3,'courseCos2':courseCos2,"mark_noti":mark_noti,'class3':class3,'class4':class4,"assName":assName,
    "studentName":studentName,'s_id':s_id,"cos_list2":cos_list2,
    'classSemester':classSemester,'weight3':weight3,"student1":student1,'ass2':ass2,'x':x})






def weight(request,x):

    roule1=rouleW.objects.all()

    for roule4 in roule1:

        p=roule4.roulesPoint


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

    others_assesments_mark1=others_assesments_mark.objects.all()
    others_assesments_mark2=others_assesments_mark1.filter(others_assid=x)
    print()
    
    
   
    xx=0
    yy=0
    if request.method=="POST":
        for ass in exam:
            x1=0
            for co in classco2:
                co1=co.classCosname
                p=ass.ass_name+co.classCosname

                p=request.POST[p]

                #print(p)
                x1=float(x1)+float(p)
                student=co_wieght.filter(asses_name=ass.ass_name)
                student1=student.filter(co_name=co1)
                for i in student1:
                    member = lms_wieght.objects.get(id=i.id)
                    member.asses_point = p
                    #member.save()
                #print("x1",x1,ass.ass_name)
            others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=ass.ass_name)
            for o in others_assesments_mark3:
                p2=ass.ass_name+"Others"
                p2=request.POST[p2]
                print(p2)
                others=others_assesments_mark.objects.get(id=o.id)
                others.others_ass_point=p2
                #others.save()

                xx=float(xx)+float(others.others_ass_point)

            total3=total.filter(Exam_name=ass.ass_name)
            #print(total3)
            for t in total3:
                
                r=t.Exam_name
                
                ratio=request.POST[r]
                total5=wieght_number.objects.get(id=t.id)
                total5.taken=x1
                total5.ratio=ratio
                total5.wieght=float(ratio)*float(x1)
                #print("xx1",xx)
                xx=float(xx)+float(total5.wieght)
                #print(xx)
                #total5.save()
        ############################################
        if(xx<=100):
            xx=0
            for ass in exam:
                x1=0
                for co in classco2:
                    co1=co.classCosname
                    p=ass.ass_name+co.classCosname
                    p=request.POST[p]

                    #print(p)
                    x1=float(x1)+float(p)
                    student=co_wieght.filter(asses_name=ass.ass_name)
                    student1=student.filter(co_name=co1)
                    for i in student1:
                        member = lms_wieght.objects.get(id=i.id)
                        member.asses_point = p
                        member.save()
                
                    #print("x1",x1,ass.ass_name)
                    
                total3=total.filter(Exam_name=ass.ass_name)
                #print(total3)
                for t in total3:
                
                    r=t.Exam_name
                
                    ratio=request.POST[r]
                    total5=wieght_number.objects.get(id=t.id)

                    total5.taken=x1
                    total5.ratio=ratio

                    p2=ass.ass_name+"Others"
                    p2=request.POST[p2]
                    print(p2)
                    total5.taken=float(x1)+float(p2)

                    others_assesments_mark3=others_assesments_mark2.filter(others_ass_name=ass.ass_name)

                    

                    for o in others_assesments_mark3:
                        
                        others=others_assesments_mark.objects.get(id=o.id)
                        others.others_ass_point=p2
                        others1=others.others_ass_point
                        others.save()
                        
                        x1=float(x1)+float(others1)
                    #print("xx1",xx)
                    total5.wieght=float(ratio)*float(x1)
                    xx=float(xx)+float(total5.wieght)
                    print(xx)
                    total5.save()        
            
            #print(x1)
            for weight_ass4 in weightx1:
                weight_ass3=weight_ass.objects.get(id=weight_ass4.id)
                weight_ass3.totalweight=xx
                weight_ass3.save()

            noti=1
        else:
            noti=2

        total=total2.filter(class_id=x)
        weightx1=weightx.filter(wieghtClassid=x)

        

        lms_wieght1=lms_wieght.objects.all()
        lms_wieght2=lms_wieght1.filter(classid=x)

        classco1=classco.objects.all()
        classco2=classco1.filter(classId=x)

        for co1 in classco2:
            lms_wieght3=lms_wieght2.filter(co_name=co1.classCosname)
            comark=0
            for lms_wieght4 in lms_wieght3:
                comark=float(lms_wieght4.asses_point)+float(comark)
                
            classco11=classco.objects.get(id=co1.id)
            classco11.classCosmark=comark
            classco11.save()
            
        classco2=classco1.filter(classId=x)

        roule1=rouleW.objects.all()

        for roule4 in roule1:

            p=roule4.roulesPoint

        
        classcopomaping1=classcopomaping.objects.all()
        classcopomaping2=classcopomaping1.filter(copomapingCc=x)



        classPo1=classPo.objects.all()
        classPo2=classPo1.filter(classPoId=x)
        
        for po in classPo2:
            po1=po.classPosname
            classcopomaping3=classcopomaping2.filter(copomapingpo=po1)
            com=0
            for classcopomaping4 in classcopomaping3:
                co=classcopomaping4.copomapingCo
                classco3=classco2.filter(classCosname=co)
                for co4 in classco3:
                    com=float(com)+co4.classCosmark
            
            pom=classPo.objects.get(id=po.id)
            pom.classPosmark=com
            pom.save()







        return render(request ,'wieght.html',{ "p":p,"others_assesments_mark2":others_assesments_mark2, 'classco2':classco2,'x':x ,'co_lis':co_lis,'noti':noti, 'class3':class3, 'exam':exam ,'weight2':weight2,'total':total,'sec':sec, 'weightx1':weightx1,'courseCos2':courseCos2 })
    noti=""

    return render(request ,'wieght.html',{"p":p,"others_assesments_mark2":others_assesments_mark2,'classco2':classco2,'x':x ,'co_lis':co_lis,'noti':noti, 'class3':class3, 'exam':exam ,'weight2':weight2,'total':total,'sec':sec,'weightx1':weightx1,'courseCos2':courseCos2  })



def profile(request):

    email=request.session['name']
    teacher_list=add_teachers.objects.all()
    teach=teacher_list.filter(tp_email=email)
    for t in teach:
        firstName=t.tfirstName
        lastName=t.tlastName
        t_id=t.t_id
        tCode=t.tCode
        tphone=t.tphone
        tdep=t.tdep



    return render(request ,'profile.html',{'email':email,'firstName':firstName,
    'lastName':lastName,'t_id':t_id,'tCode':tCode,'tphone':tphone,'tdep':tdep})











##################################################################
def update(request,x,pk):
    

    return render(request ,'teacherHome.html')

    
def teachersFeadback1(request,x,code,sec):
    fednoti=""

    teachersFeadback1=teachersFeadback.objects.all()

    if request.method=="POST":
        email=request.session['name']

        teachersFeadbackId=x

        teachersId=email

        teachersFeadbackcourse=code
        teachersFeadbacksec=sec


        teacherFeadback=request.POST['teacherFeadback']

        if(teachersFeadback1.filter(teachersFeadbackId=x)):
            fednoti=0
        else:
            fednoti=1
            addfed=teachersFeadback(teachersFeadbackId=teachersFeadbackId,teachersFeadbackcourse=teachersFeadbackcourse,teachersFeadbacksec=teachersFeadbacksec,teachersId=teachersId,teacherFeadback=teacherFeadback)
            addfed.save()

    
    #teachersId=




    return render(request ,'teachersFeadback.html',{"x":x,"code":code,"sec":sec,"fednoti":fednoti})

def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully logout!')
    return redirect("signup")
