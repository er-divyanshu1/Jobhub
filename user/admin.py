from django.contrib import admin

from .models import StudentUser,Recruiter,Job,ContactUs,SelectedStudent,Apply

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Recruiter)
admin.site.register(Job) 
admin.site.register(ContactUs)
admin.site.register(SelectedStudent)
admin.site.register(Apply)