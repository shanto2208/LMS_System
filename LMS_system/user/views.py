from contextlib import _RedirectStream, redirect_stderr
import email
from pickle import NONE
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact_us, stuser,adminuser, teachuser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from result.views import add_student, add_teachers


# Create your views here.

def signup(request):
    if request.method=="POST":
        u_email=request.POST["userEmail"]
        student_list=add_student.objects.all()
        if student_list.filter(p_email=u_email):
            student=stuser.objects.all()
            if student.filter(useremail = u_email):
                return render(request ,'signup.html')
            else:
                request.session['name'] = u_email
                print(request.session['name'])
                return redirect('user_signup')

        elif request.method=="POST":
            teacher_list=add_teachers.objects.all()
            if teacher_list.filter(tp_email=u_email):
                teacher=teachuser.objects.all()
                if teacher.filter(teachemail = u_email):
                    return render(request ,'signup.html')
                else:
                    request.session['name'] = u_email
                    print(request.session['name'])
                    return redirect('user_signup')
    return render(request ,'signup.html')

    

def user_login(request):
#    if request.method=="POST":
  #      form=AuthenticationForm(request=request, data=request.POST)
  #      if form.is_valid():
  #          username=form.cleaned_data.get('username')
   #         password=form.cleaned_data.get('password')
    #        user=authenticate(username=username,password=password)
     #       if user is not None:
      #          login(request,user)
       #         return redirect('home')
#            else:
 #               messages.error(request, 'Invalid Username or password')
 #      else:
 #          messages.error(request, 'Invalid Username or password')
 #  else:
 #       form=AuthenticationForm()
 #      return render(request ,'login.html',{'form':form})
   return render(request ,'login.html')


def contact(request):
    if request.method=="POST":
        email=request.POST["email"]
        name=request.POST["name"]
        problem=request.POST["problem"]
        obj=Contact_us(email=email,name=name,problem=problem)
        obj.save()
    return render(request ,'contact.html')

def user_signup(request):
    if request.method=="POST":
        student_list=add_student.objects.all()
        useremail=request.POST["useremail"]
        firstpass=request.POST["firstpass"]
        secpass=request.POST["secpass"]
        if student_list.filter(p_email=useremail):
            student=stuser.objects.all()
            if student.filter(useremail=useremail):
                print("id uniq ")
            else:
                if (len(secpass)>=8):
                    if firstpass==secpass:
                        print("user save")
                        user=stuser(useremail=useremail,userpass=firstpass)
                        user.save()
                        request.session['user'] = useremail
                        return redirect('studentHome')

        elif request.method=="POST":
            teacher_list=add_teachers.objects.all()
            if teacher_list.filter(tp_email=useremail):
                teacher=teachuser.objects.all()
                if teacher.filter(teachemail=useremail):
                    print("id not uniq ")
                else:
                    if (len(secpass)>=8):
                        if firstpass==secpass:
                            print("user save")
                            user=teachuser(teachemail=useremail,teachpass=firstpass)
                            user.save()
                            request.session['user'] = useremail
                            return redirect('teacherHome')
    #student_list=add_student.objects.all()
    #u_email=request.GET.get('userEmail')
    #if student_list.filter(p_email=u_email):
    #    request.session['name'] = u_email
    #    u_email=request.GET.get('userEmail')
     #   u_email=request.GET.get('userEmail')
    #else:
        #en_pass=pbkdf2_sha256.encrypt(firstpass)
        #en_pass2=pbkdf2_sha256.encrypt(secpass)
        #print(en_pass)
        #print(en_pass2)
    return render(request ,'user_login.html')

def login(request):
    if request.method=="POST":
        student_list=stuser.objects.all()
        user_email=request.POST["user_email"]
        first_pass=request.POST["first_pass"]
        if student_list.filter(useremail=user_email):
            if student_list.filter(userpass=first_pass):
                request.session['name'] = user_email
                return redirect('studentHome')
        elif request.method=="POST":
            print("pass")
            admin_list=adminuser.objects.all()
            if admin_list.filter(adminemail=user_email):
                print("pass")
                if admin_list.filter(adminpass=first_pass):
                    print("pass2")
                    request.session['name'] = user_email
                    return redirect('home')

            elif request.method=="POST":
                print("pass")
                teacher_list=teachuser.objects.all()
                print("pass")
                if teacher_list.filter(teachemail=user_email):
                    print("pass")
                    if teacher_list.filter(teachpass=first_pass):
                        print("pass2")
                        request.session['name'] = user_email
                        return redirect('teacherHome')
    return render(request ,'adstlogin.html')