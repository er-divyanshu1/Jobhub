from django.contrib import admin
from django.urls import path
from jobhub import settings
from user.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contact_us', contact_us, name="contact_us"),
    path('contact_ususer', contact_ususer, name="contact_ususer"),
    path('job_list', job_list, name="job_list"),

    #User Url

    path('user_login', user_login, name="user_login"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_edit_profile', user_edit_profile, name="user_edit_profile"),
    path('user_change_password', user_change_password, name="user_change_password"),
    path('user_home', userhome, name="user_home"),
    path('user_profile', user_profile, name="user_profile"),
    path('user_joblist', user_joblist, name="user_joblist"),
    path('job_detail/<int:pid>', job_detail, name="job_detail"),
    path('applied_job_detail/<int:pid>', applied_job_detail, name="applied_job_detail"),
    path('apply_for_job/<int:jid>', apply_for_job, name="apply_for_job"),

    #Recruiter Url

    path('recruiter_login', recuiter_login, name="recruiter_login"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('recruiter_profile', recruiter_profile, name="recruiter_profile"),
    path('recruiter_edit_profile', recruiter_edit_profile, name="recruiter_edit_profile"),
    path('jobpost', jobpost, name="jobpost"),
    path('jobpost_edit/<int:pid>', jobpost_edit, name="jobpost_edit"),
    path('delete/<int:id>', delete, name="delete"),
    path('recruiter_change_password', recruiter_change_password, name="recruiter_change_password"),
    path('applyed_condidate_list', applyed_condidate_list, name="applyed_condidate_list"),
    #Logout Url
   path('logout', logoutPage, name='logout'),

]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
