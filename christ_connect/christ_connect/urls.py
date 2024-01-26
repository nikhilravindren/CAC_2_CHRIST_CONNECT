"""
URL configuration for christ_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import job,jobposting,jobsearch,jobcategory,details,fulljob , user_user_login,editprofile,home,addprofile,posts,profile,like_post,comment,peoples,followes,connections,applyjob,user_message,send_message,about,send_admin
                             
from cadmin.views import Dashboard,table , statuschange , edituser , user_login ,deleteprofile,profiletable,jobtable,deletejob,posttable,post_status,liketable,likestatus,comment_table,deletecomment,profileadd,adduser,edit_profile,noti_change,noti_table,notifi_change,alumni,jobedit,follow_bridge,unfollow,msg_delete,msg_table,admin_msg,solve
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
# Students
    path('admin/', admin.site.urls),
    path('',user_user_login,name='user_user_login'),
    path('job' , job , name="job"),
    path('jobposting',jobposting,name="jobposting"),
    path('jobsearch',jobsearch,name="jobsearch"),
    path('jobcategory/<str:id>',jobcategory,name='jobcategory'),
    path('details/<int:id>',details,name='details'),
    path("fulljobs",fulljob,name='fulljob'),
    path("applyjob/<int:id>",applyjob,name='applyjob'),
    path("about",about,name='about'),

    #user
    path('home',home,name='home'),
    path('profile',profile,name='profile'),
    path('edit',editprofile,name='edit'),
    path('add',addprofile,name='add'),
    path('post',posts,name='post'),
    path('like/<int:id>/', like_post, name='like'),
    path('comment/<int:id>/',comment, name='comment'),
    path('peoples',peoples,name='peoples'),
    path('follow/<int:id>/',followes, name='follow'),
    path('connections',connections, name='connections'),
    path('user_message/<int:id>/',user_message, name='user_message'),
    path('send_message/<int:id>/',send_message, name='send_message'),
    path('send_admin',send_admin, name='send_admin'),
    path('solve/<int:id>/',solve, name='solve'),
    
    # login
    path('user_login' , user_login , name="user_login"),

# Admin
    path('cadmin/Dashboard', Dashboard, name = "dashboard"),
    path('cadmin/table', table, name = "table"),
    path('cadmin/statuschange/<int:user_id>' , statuschange , name="statuschange"),
    path('cadmin/edituser/<int:user_id>' , edituser , name="edituser"),
    path('cadmin',user_login,name='user_login'),
    path('cadmin/deleteprofile/<int:id>',deleteprofile, name='deleteprofile'),
    path('cadmin/profiletable',profiletable, name='profiletable'),
    path('cadmin/jobtable',jobtable, name='jobtable'),
    path('cadmin/deletejob/<int:id>',deletejob, name='deletejob'),
    path('cadmin/editjob/<int:id>',jobedit, name='editjob'),
    path('cadmin/poststable',posttable, name='posttable'),
    path('cadmin/poststatus/<int:id>',post_status, name='poststatus'),
    path('cadmin/liketable',liketable, name='liketable'),
    path('cadmin/likestatus/<int:id>',likestatus, name='likestatus'),
    path('cadmin/comment_table',comment_table, name='commenttable'),
    path('cadmin/commentdelete/<int:id>',deletecomment, name='deletecomment'),
    path('cadmin/profileadd',profileadd, name='profileadd'),
    path('cadmin/useradd',adduser, name='adduser'),
    path("edit_profile/<int:id>",edit_profile,name='edit_profile'),
    path("noti_change/<int:id>",noti_change,name='noti_change'),
    path("cadmin/noti_table",noti_table,name='noti_table'),
    path("notifi_change/<int:id>",notifi_change,name='notifi_change'),
    path("alumni/<int:id>",alumni,name='alumni'),
    path("follow_bridge",follow_bridge,name='follow_bridge'),
    path("status_change/<int:id>",unfollow,name='unfollow'),
    path("msg_delete/<int:id>",msg_delete,name='msg_delete'),
    path("msg_table",msg_table,name='msg_table'),
    path("admin_msg",admin_msg,name='admin_msg'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
