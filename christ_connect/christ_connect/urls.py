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
from students.views import job,jobposting,jobsearch,jobcategory,details,fulljob , user_user_login,editprofile,home,addprofile
from cadmin.views import Dashboard,table , statuschange , edituser , user_login 
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

    #user
    path('home',home,name='home'),
    path('edit',editprofile,name='edit'),
    path('add',addprofile,name='add'),
    
    # login
    path('user_login' , user_login , name="user_login"),

# Admin
    path('cadmin/Dashboard', Dashboard, name = "dashboard"),
    path('cadmin/table', table, name = "table"),
    path('cadmin/statuschange/<int:user_id>' , statuschange , name="statuschange"),
    path('cadmin/edituser/<int:user_id>' , edituser , name="edituser"),
    path('cadmin',user_login,name='user_login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
