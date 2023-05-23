from django.db import models


# Create your models here.


class add_student(models.Model):

    firstName=models.CharField(max_length=40,default="null")
    lastName=models.CharField(max_length=40)
    s_id=models.CharField(max_length=20,primary_key=True)
    b_date=models.CharField(max_length=20, default="null")
    gender=models.CharField(max_length=20)
    p_email=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    dep=models.CharField(max_length=40)
    seme=models.CharField(max_length=20)



class add_course(models.Model):
    courseName=models.CharField(max_length=250)
    courseCode=models.CharField(max_length=40, primary_key=True)
    depname=models.CharField(max_length=40, default="null")
    credit=models.CharField(max_length=20)



class add_teachers(models.Model):
    tfirstName=models.CharField(max_length=40)
    tlastName=models.CharField(max_length=40)
    t_id=models.CharField(max_length=20, primary_key=True)
    tgender=models.CharField(max_length=20,default="null")
    tp_email=models.CharField(max_length=90)
    tphone=models.CharField(max_length=15)
    tdep=models.CharField(max_length=40)
    tCode=models.CharField(max_length=40)


class classTime(models.Model):
    classTime=models.CharField(max_length=20)
    labTime=models.CharField(max_length=20)


class clsRoom(models.Model):
    classCode= models.CharField(max_length=250,primary_key=True)
    classSemester= models.CharField(max_length=40)
    courseCod= models.CharField(max_length=40)
    coursesec=models.CharField(max_length=40)
    instructor= models.CharField(max_length=40)
    tClassTime=models.CharField(max_length=40)
    labClassTime=models.CharField(max_length=40)


class duptclsRoom(models.Model):
    dupclassName= models.CharField(max_length=40)
    dupclassCode= models.CharField(max_length=40)
    dupclassSemester= models.CharField(max_length=40)
    dupcourseCod= models.CharField(max_length=40)
    dupcoursesec=models.CharField(max_length=40)
    dupinstructor= models.CharField(max_length=40)
    duptClassTime=models.CharField(max_length=40)
    duplabClassTime=models.CharField(max_length=40)


class semester(models.Model):
    semester=models.CharField(max_length=40)
    studentamount=models.CharField(max_length=40,default="0")


#  class model model
class clsStudent(models.Model):
    stdid=models.CharField(max_length=40)
    classCod=models.CharField(max_length=40)


class dept(models.Model):
    dept_name=models.CharField(max_length=40)
    dep_title=models.CharField(max_length=225)
    dept_cradit=models.CharField(max_length=40)
    dep_numberOfstudent=models.CharField(max_length=40, default="0")
    dep_numberOfCourse=models.CharField(max_length=40, default="0")
    dep_numberOfTeacher=models.CharField(max_length=40, default="0")


class cos(models.Model):
    co_name=models.CharField(max_length=40)
    co_descriptions=models.CharField(max_length=200)
    co_depname=models.CharField(max_length=100)


class pos(models.Model):
    po_name=models.CharField(max_length=40)
    po_descriptions=models.CharField(max_length=200)
    po_depname=models.CharField(max_length=100)


class assesment_mark(models.Model):
    classId=models.CharField(max_length=20)
    studentId=models.CharField(max_length=20)
    assesmentName=models.CharField(max_length=20,default="null")
    coName=models.CharField(max_length=20)
    mark=models.FloatField(max_length=20)


class greading(models.Model):
    firstMark=models.CharField(max_length=20)
    secMark=models.CharField(max_length=20)
    greadLetter=models.CharField(max_length=20)
    gpa=models.CharField(max_length=20,default="null")


class copomaping(models.Model):
    copomapingCc=models.CharField(max_length=20)
    copomapingCo=models.CharField(max_length=20)
    copomapingpo=models.CharField(max_length=20)


class classcopomaping(models.Model):
    copomapingCc=models.CharField(max_length=20)
    copomapingCo=models.CharField(max_length=20)
    copomapingpo=models.CharField(max_length=20)


class courseCos(models.Model):
    courseCos_id=models.CharField(max_length=200) #course code
    courseCosname=models.CharField(max_length=40)
    courseCosmark=models.FloatField(max_length=20,default='0')


class coursePos(models.Model):
    coursePos_id=models.CharField(max_length=200) #course code
    coursePosname=models.CharField(max_length=40)
    coursePosmark=models.FloatField(max_length=20,default='0')


class classco(models.Model):
    classId=models.CharField(max_length=200)
    classCosname=models.CharField(max_length=40)
    classCosmark=models.FloatField(max_length=20 , default='0')


class classPo(models.Model):
    classPoId=models.CharField(max_length=200)
    classPosname=models.CharField(max_length=40)
    classPosmark=models.FloatField(max_length=20,default='0')
    

class coAttainment(models.Model):
    coAttainmentId=models.CharField( max_length = 200 )
    coAttainmentCosname=models.CharField( max_length = 40 )
    coAttainmentCosmark=models.FloatField( max_length = 20 , default='0')
    coAttainmentAttainment=models.CharField( max_length = 20 , default='0')

class pOAttainment(models.Model):
    pOAttainmentId=models.CharField( max_length = 200 )
    pOAttainmentCosname=models.CharField( max_length = 40 )
    pOAttainmentCosmark=models.FloatField( max_length = 20 , default='0')
    pOAttainmentAttainment=models.CharField( max_length = 20 , default='0')



#class copomap()
class others_assesment_mark(models.Model):
    others_classId=models.CharField(max_length=20)
    others_studentId=models.CharField(max_length=20)
    others_assesmentName=models.CharField(max_length=20,default="null")
    others_coName=models.CharField(max_length=20)
    others_mark=models.FloatField(max_length=20)


class course_assesments_mark(models.Model):
    course_assid=models.CharField(max_length=250)#classCode
    course_ass_name=models.CharField(max_length=20)
    course_ass_point=models.CharField(max_length=3)


class others_course_assesments_mark(models.Model):
    others_course_assid=models.CharField(max_length=250)#classCode
    others_course_ass_name=models.CharField(max_length=20)
    others_course_others_name=models.CharField(max_length=20,default="Others")
    others_course_ass_point=models.FloatField(max_length=20)


class course_wieght_number(models.Model):
    course_class_id=models.CharField(max_length=250)
    course_Exam_name=models.CharField(max_length=20)
    course_wieght=models.FloatField(max_length=20,default="0")
    course_taken=models.FloatField(max_length=3,default="0")
    course_ratio=models.FloatField(max_length=3,default="0")


class course_lms_wieght(models.Model):
    course_classid=models.CharField(max_length=250)
    course_asses_name=models.CharField(max_length=20)
    course_co_name=models.CharField(max_length=20 ,default="null")
    course_asses_point=models.FloatField(max_length=3)


class course_wieght_total(models.Model):
    totalClassid=models.CharField(max_length=250)
    totalAsses_name=models.CharField(max_length=20)
    totalCo_name=models.CharField(max_length=20 ,default="null")
    totalpoint=models.FloatField(max_length=3,default="0")


class course_weight_ass(models.Model):
    wieghtClassid=models.CharField(max_length=250)
    totalweight=models.FloatField(max_length=20)


class others_assesments_mark(models.Model):
    others_assid=models.CharField(max_length=250)#classCode
    others_ass_name=models.CharField(max_length=20)
    others_others_name=models.CharField(max_length=20,default="Others")
    others_ass_point=models.FloatField(max_length=20)


class teachersFeadback(models.Model):
    teachersFeadbackId=models.CharField(max_length=250)#classCode
    teachersFeadbackcourse=models.CharField(max_length=250,default="null")
    teachersFeadbacksec=models.CharField(max_length=250,default="null")
    teachersId=models.CharField(max_length=250)
    teacherFeadback=models.CharField(max_length=550)



