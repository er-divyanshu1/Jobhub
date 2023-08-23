from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
import datetime
from datetime import date

# Create your views here.
def index(request):
    student = SelectedStudent.objects.all().order_by('id')[:5]
    job = Job.objects.all().order_by('id')[:20]
    data={'student':student,'job':job}
    
    return render(request,"index.html",data)

def user_login(request):
    if request.method=='POST' :
       uname = request.POST['email']
       pass1 = request.POST['pass']
       user= authenticate (username= uname, password=pass1)
       if User:
           try:
               user1=StudentUser.objects.get(user=user)
               if user1.type=="Student":
                   login(request,user)
                   
                   return redirect('user_home')
               else:
                   messages.success(request,'Somthig went Wrong.')
           except:
               messages.warning(request,'Somthig went Wrong.')
       else:
           messages.warning(request,'Somthig went Wrong.')
    
    return render(request,"user_login.html")

def recuiter_login(request):
    if request.method=='POST' :
       uname = request.POST['email']
       pass1 = request.POST['pass']
       user= authenticate (username= uname, password=pass1)
       if User:
           try:
               user1=Recruiter.objects.get(user=user)
               if user1.type=="Recruiter" and user1.status!="pending":
                   login(request,user)
                   return redirect('recruiter_home')
                   
               else:
                   messages.warning(request,'user peding.')
           except:
               messages.warning(request,'Somthig went Wrong.')
       else:
           messages.warning(request,'Somthig went Wrong.')
    
    return render(request,"recruiter_login.html")

def user_signup(request):
    error= ""
    if request.method=='POST' :
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       email = request.POST['email']
       phone = request.POST['phone']
       img = request.FILES['image']
       gender = request.POST['gender']
       p1 = request.POST['pass1']
       p2 = request.POST['pass2']

       if p1 != p2:
            messages.warning(request,'Password is does not match.')
            return redirect('signup')
       elif User.objects.filter(username=email).exists():
           messages.warning(request,'Email allredy taken')
           return redirect('signup')
       else:
            try:
                user=User.objects.create_user(first_name=fname,last_name=lname, username=email, password=p1)
                StudentUser.objects.create(user=user, mobile=phone, type="Student", image=img,gender=gender)
                messages.success(request,'User registerd successfull.')
                return redirect('user_login')
            except:
                messages.warning(request,'Something  Wrong...')
            
    return render(request,"user_signup.html")

def recruiter_signup(request):
    if request.method=='POST' :
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       email = request.POST['email']
       phone = request.POST['phone']
       img = request.FILES['image']
       gender = request.POST['gender']
       company =request.POST['company']
       p1 = request.POST['pass1']
       p2 = request.POST['pass2']

       if p1 != p2:
            messages.warning(request,'Password is does not match.')
            return redirect('recruiter_signup')
       elif User.objects.filter(username=email).exists():
           messages.warning(request,'Email allredy taken')
           return redirect('recruiter_signup')
       else:
            try:
                user=User.objects.create_user(first_name=fname,last_name=lname, username=email, password=p1)
                Recruiter.objects.create(user=user, mobile=phone, type="Recruiter", image=img,gender=gender,company=company,status="pending",)
                messages.success(request,'Successfull.')
                return redirect('recruiter_login')
            except:
                messages.warning(request,'Something  Wrong...')
            
    return render(request,"recruiter_signup.html")

def jobpost(request): 
    if request.method=='POST' :
       Job_title = request.POST['Job_title']
       salary = request.POST['salary']
       sdate =request.POST['sdate']
       edate =request.POST['edate']
       location = request.POST['location']
       skill = request.POST['skill']
       education = request.POST['education']
       image = request.FILES['image']
       experince =request.POST['experince']
       discription = request.POST['discription']
       user1= request.user
       recruiter= Recruiter.objects.get(user=user1)
       try:
            print(recruiter)
            job=Job.objects.create(recruiter=recruiter, s_date=sdate,
            e_date=edate, job_title=Job_title, salary=salary,img=image,
            discription=discription, location=location, education=education,
            skill=skill, experince=experince )
            job.save()
            print(job)
            messages.success(request,'Job successfuly posted.')
            return redirect('recruiter_home')
       except:
            messages.warning(request,'Something  Wrong...')
    return render(request,"jobpost.html")

@login_required(login_url='user_login')
def userhome(request):
    job = Job.objects.all().order_by('s_date')[:10]
    user=request.user
    student=StudentUser.objects.get(user=user)
    d=Apply.objects.filter(student=student)
    li=[]
    for i in d:
        li.append(i.job.id)
    data={'job':job,'li':li}
    return render(request,"user_home.html",data)

@login_required(login_url='recruiter_login')
def recruiter_home(request):
    u= request.user
    recuriter= Recruiter.objects.get(user=u)
    job=Job.objects.filter(recruiter=recuriter)
    
    data={'job':job,}

    return render(request,"recruiter_home.html",data)

def logoutPage(request):
    logout(request)
    messages.warning(request,'You are logout')
    return redirect('index')

@login_required(login_url='user_login')
def user_profile(request):
    user1= request.user
    student= StudentUser.objects.get(user=user1)
    
    data={'student':student,}
    return render(request,"user_profile.html",data)

@login_required(login_url='recruiter_login')
def recruiter_profile(request):
    recuriter= request.user
    recuriter= Recruiter.objects.get(user=recuriter)
    data={'recuriter':recuriter,}
    
    return render(request,"recruiter_profile.html",data)

@login_required(login_url='recruiter_login')
def recruiter_edit_profile(request):
    recuriter= request.user
    recuriter= Recruiter.objects.get(user=recuriter)
    data={'recuriter':recuriter,}
    if request.method=='POST' :
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       phone = request.POST['phone']
       gender = request.POST['gender']
       company =request.POST['company']

       recuriter.user.first_name = fname
       recuriter.user.last_name = lname
       recuriter.mobile = phone
       recuriter.company = company
       recuriter.gender = gender
       recuriter.user.first_name = fname
       try:
            recuriter.save()
            recuriter.user.save()
            messages.success(request,' Your Profile Successfully Updated.')
            
       except:
            messages.warning(request,'Something  Wrong...')
       try:
            img = request.FILES['image']
            recuriter.image = img
            recuriter.save()
       except:
            pass
       messages.success(request,' Your Profile Successfully Updated.')
       return redirect('recruiter_profile',)
    return render(request,"recruiter_edit_profile.html",data)

@login_required(login_url='user_login')
def user_edit_profile(request):
    student= request.user
    recuriter= StudentUser.objects.get(user=student)
    data={'recuriter':recuriter,}
    if request.method=='POST' :
       fname = request.POST['first_name']
       lname = request.POST['last_name']
       phone = request.POST['phone']
       gender = request.POST['gender']

       recuriter.user.first_name = fname
       recuriter.user.last_name = lname
       recuriter.mobile = phone
       recuriter.gender = gender
       try:
            recuriter.save()
            recuriter.user.save()
            
            
       except:
            messages.warning(request,'Something  Wrong...')
       try:
            img = request.FILES['image']
            recuriter.image = img
            recuriter.save()
       except:
            pass
       messages.success(request,' Your Profile Successfully Updated.')
       return redirect('user_profile',)
    return render(request,"user_edit_profile.html",data)

@login_required(login_url='user_login')
def user_change_password(request):
    if request.method=='POST' :
       p1 = request.POST['pass1']
       p2 = request.POST['pass2']
       p3 = request.POST['pass3']
       try:
            u=User.objects.get(id=request.user.id)
            if p2 != p3:
                messages.warning(request,'Password and Confirm Password did not match.')
                return redirect('user_change_password')
                
            elif u.check_password(p1):
                u.set_password(p2)
                u.save()
                pass
                messages.success(request,'User new password  successfuly udated.')
                
            else:
                messages.warning(request,'User old password is wrong')
                return redirect('user_change_password')
       except:
            messages.warning(request,'Something  Wrong...')

       
    return render(request,"user_change_password.html")

@login_required(login_url='recruiter_login')
def recruiter_change_password(request):
    if request.method=='POST' :
       p1 = request.POST['pass1']
       p2 = request.POST['pass2']
       p3 = request.POST['pass3']
       try:
            u=User.objects.get(id=request.user.id)
            if p2 != p3:
                messages.warning(request,'Password and Confirm Password did not match.')
                return redirect('user_change_password')
                
            elif u.check_password(p1):
                u.set_password(p2)
                u.save()
                pass
                messages.success(request,'User new password  successfuly udated.')
                
            else:
                messages.warning(request,'User old password is wrong')
                return redirect('user_change_password')
       except:
            messages.warning(request,'Something  Wrong...')
    
    return render(request,"recruiter_change_password.html")

@login_required(login_url='recruiter_login')
def jobpost_edit(request,pid):
    job= Job.objects.get(id=pid)
    data={'job':job}

    if request.method=='POST' :
       Job_title = request.POST['Job_title']
       salary = request.POST['salary']
       sdate =request.POST['sdate']
       edate =request.POST['edate']
       location = request.POST['location']
       skill = request.POST['skill']
       education = request.POST['education']
    
       experince =request.POST['experince']
       discription = request.POST['discription']

       job.job_title=Job_title
       job.discription=discription
       job.location=location
       job.education=education
       job.salary=salary
       job.skill=skill
       job.experince=experince

       try:
            job.save()
       except:
            messages.warning(request,'Something  Wrong...')
       try:
            img = request.FILES['image']
            job.img=img
            job.save()
       except:
            pass
       if edate:
            try:
                job.e_date=edate
                job.save()
            except:
                pass
       else:
           pass
       
       if sdate:
            try:
                job.s_date=sdate
                job.save()
               
            except:
                pass
       else:
           pass
       messages.success(request,'Job successfuly Updated.')
       return redirect('recruiter_home')
    return render(request,"jobpost_edit.html",data)

def delete(request,id):
    job= Job.objects.get(id=id)
    job.delete()
    messages.success(request,'Job successfuly Deleted.')
    return redirect('recruiter_home',)

@login_required(login_url='user_login')
def user_joblist(request):
    job = Job.objects.all().order_by('s_date')
    user=request.user
    student=StudentUser.objects.get(user=user)
    d=Apply.objects.filter(student=student)
    li=[]
    for i in d:
        li.append(i.job.id)
    data={'job':job,'li':li}
    return render(request,"user_joblist.html",data)

def job_list(request):
    job = Job.objects.all().order_by('s_date')
    data={'job':job,}
    return render(request,"job_list.html",data)

@login_required(login_url='user_login')
def job_detail(request,pid):
    job= Job.objects.get(id=pid)
    data={'job':job}

    return render(request,'job_detail.html',data)

@login_required(login_url='user_login')
def applied_job_detail(request,pid):
    job= Job.objects.get(id=pid)
    data={'job':job}

    return render(request,'applied_job_detail.html',data)

def contact_us(request):
    if request.method=='POST' :
       n = request.POST['name']
       e = request.POST['email']
       m = request.POST['message']
       try:
                cn=ContactUs.objects.create(name=n,email=e, message=m)
                cn.save()
                messages.success(request,'Thanks For Contact Me !')
                return redirect('contact_us')
       except:
                messages.warning(request,'Something  Wrong...')
    return render(request,'contact_us.html')

@login_required(login_url='user_login')
def contact_ususer(request):
    if request.method=='POST' :
       n = request.POST['name']
       e = request.POST['email']
       m = request.POST['message']
       try:
                cn=ContactUs.objects.create(name=n,email=e, message=m)
                cn.save()
                messages.success(request,'Thanks For Contact Me !')
                return redirect('contact_ususer')
       except:
                messages.warning(request,'Something  Wrong...')
    return render(request,'contact_ususer.html')

@login_required(login_url='user_login')
def apply_for_job(request,jid):
    job= Job.objects.get(id=jid)
    user= request.user
    student=StudentUser.objects.get(user=user)
    data={'job':job}
    date1 = date.today()
    if job.e_date < date1:
        messages.success(request,'Job date exapire, you can not apply this job.')
        return redirect(user_joblist)
    elif job.s_date > date1:
        messages.success(request,'Job date not start today , Plz Try affter same days.')
        return redirect(user_joblist)
    else:
        if  request.method=='POST':
            resume= request.FILES['resume']
            Apply.objects.create(student=student, job=job, resume=resume, applydate=date1.today())
            messages.success(request,'Congratulation ! your resume successfully uploaded  for this job.')

    
    return render(request,'apply_for_job.html',data)

@login_required(login_url='recruiter_login')
def applyed_condidate_list(request):
    
    d=Apply.objects.all()
    data={'d':d,}
   
    return render(request,'applyed_condidate_list.html',data)
