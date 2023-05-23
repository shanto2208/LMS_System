from django.db import models


# Create your models here.

class add_student(models.Model):
    firstName=models.CharField(max_length=40)
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


class courseCos(models.Model):
    courseCos_id=models.CharField(max_length=200)#course code
    courseCosname=models.CharField(max_length=40)



class classco(models.Model):
    classId=models.CharField(max_length=200)
    classCosname=models.CharField(max_length=40)
    classCosmark=models.FloatField(max_length=20,default='0')


#class copomap()
