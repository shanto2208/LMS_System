from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contact_us(models.Model):
    email= models.CharField(max_length=40)
    name= models.CharField(max_length=20)
    problem= models.TextField()


# student id pass model
class stuser(models.Model):
    useremail=models.CharField(max_length=40)
    userpass=models.CharField(max_length=40)


# admin id pass model
class adminuser(models.Model):
    adminemail=models.CharField(max_length=40)
    adminpass=models.CharField(max_length=40)

    
# teacher id pass model
class teachuser(models.Model):
    teachemail=models.CharField(max_length=40)
    teachpass=models.CharField(max_length=40)
    



