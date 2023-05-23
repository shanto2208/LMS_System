from django.db import models



# Create your models here.

###############################################################

class assesments_mark(models.Model):
    assid=models.CharField(max_length=250)#classCode
    ass_name=models.CharField(max_length=20)
    ass_point=models.CharField(max_length=3)



class lms_wieght(models.Model):
    classid=models.CharField(max_length=250)
    asses_name=models.CharField(max_length=20)
    co_name=models.CharField(max_length=20 ,default="null")
    asses_point=models.FloatField(max_length=3)

class wieght_number(models.Model):
    class_id=models.CharField(max_length=250,default="null")
    Exam_name=models.CharField(max_length=20,default="null")
    wieght=models.FloatField(max_length=20,default="null")
    taken=models.FloatField(max_length=3,default="null")
    ratio=models.FloatField(max_length=3,default="null")

class wieght_total (models.Model):
    totalClassid=models.CharField(max_length=250)
    totalAsses_name=models.CharField(max_length=20)
    totalCo_name=models.CharField(max_length=20 ,default="null")
    totalpoint=models.FloatField(max_length=3,default="0")

class weight_ass(models.Model):
    wieghtClassid=models.CharField(max_length=250)
    totalweight=models.FloatField(max_length=20)

class AssMark(models.Model):
    markS_id=models.CharField(max_length=250)
    markClassId=models.CharField(max_length=20)
    markAssName=models.CharField(max_length=20)
    MarkAss=models.CharField(max_length=20)


class gread(models.Model):
    greadS_id=models.CharField(max_length=250)
    greadClassId=models.CharField(max_length=200)
    greadtotalmark=models.CharField(max_length=20)
    greadLetter=models.CharField(max_length=20)

class usersemester(models.Model):
    user_id=models.CharField(max_length=250)
    semestername=models.CharField(max_length=250)

class rouleW(models.Model):
    roulesname=models.CharField(max_length=250)
    roulesPoint=models.CharField(max_length=50)


class CoMark(models.Model):
    CoMarkClassId=models.CharField(max_length=20)
    CoMarkconame=models.CharField(max_length=20)
    CoMarks=models.CharField(max_length=20)