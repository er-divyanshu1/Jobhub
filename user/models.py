from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.CharField(max_length=15,null=True)
    image= models.FileField(null=True)
    gender= models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15)
    def __str__(self):
        return self.user.username
    
class Recruiter(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile= models.CharField(max_length=15,null=True)
    image= models.FileField(null=True)
    gender= models.CharField(max_length=10, null=True)
    company=models.CharField(max_length=50,null=True)
    type = models.CharField(max_length=15)
    status= models.CharField(max_length=20)
    def __str__(self):
        return self.user.username

class Job(models.Model):
    recruiter=models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    s_date= models.DateField()
    e_date= models.DateField()
    job_title= models.CharField(max_length=100,)
    salary= models.FloatField(max_length=50)
    img= models.FileField()
    discription = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    skill = models.CharField(max_length=200)
    experince= models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.job_title
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.email

class SelectedStudent(models.Model):
    name = models.CharField(max_length=50)
    img= models.FileField()
    company  = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    salary= models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    resume= models.FileField()
    applydate = models.DateField()
    
    
    
    