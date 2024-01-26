from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from .models import user_profile,Notifications,admin_messages
from students.models import JobPortal,user_posts,post_likes,post_comments,user_follow,messages


# Admin Panel

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user is not None and user.is_active:
            if user.is_superuser == True and user.is_staff == True:
                login(request , user)
                return redirect('dashboard')
            else:
                msg = "You are not autherized for the access!"
                return render(request , 'cadmin/Users/login.html' , {'msg':msg})
        else:
            msg = "Wrong credentials"
            return render(request , 'cadmin/Users/login.html' , {"msg":msg})
    return render(request , 'cadmin/Users/login.html')

    

@login_required(login_url = 'user_login')
def Dashboard(request):
    profile = user_profile.objects.get(user=request.user)
    notification = Notifications.objects.filter(noti_status=True)
    user_count = User.objects.count()
    post_count = user_posts.objects.count()
    job_count = JobPortal.objects.count()
    like_count = post_likes.objects.count()
    comment_count = post_comments.objects.count()
    return render(request, 'cadmin/index.html',{'profile':profile,'notification':notification,'user_count':user_count,'post_count':post_count,'job_count':job_count,'like_count':like_count,'comment_count':comment_count})

def noti_change(request,id):
    notification = Notifications.objects.get(id=id)
    notification.noti_status = False
    notification.save()
    return redirect('dashboard')

def notifi_change(request,id):
    notification = Notifications.objects.get(id=id)
    if notification.noti_status == True:
        notification.noti_status = False
    else:
        notification.noti_status = True
    notification.save()
    return redirect('noti_table')

def noti_table(request):
    notification = Notifications.objects.all()
    profile = user_profile.objects.get(user=request.user)
    return render(request,'cadmin/Users/noti-table.html',{'notification':notification,'profile':profile})


def table(request):
    users = User.objects.all()
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    return render(request, 'cadmin/Users/data-tables.html' , {'users':users,'profile':profile,'notification':notification})

def alumni(request,id):
    user = User.objects.get(id=id)
    if user.is_staff == True:
        user.is_staff =False
    else:
        user.is_staff =True
    user.save()
    return redirect('table')

def statuschange(request , user_id):
    user = User.objects.get(id = user_id)
    if user.is_active == True:
        user.is_active = False
        user.save()
        return redirect('table')
    else:
        user.is_active = True
        user.save()
        return redirect('table')

def edituser(request , user_id):
    user = User.objects.get(id = user_id)
    if request.method == "POST":
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        user.save()
        return redirect('table')
    return render(request , 'cadmin/Users/edit_user.html' , {'user':user})

def deleteprofile(request,id):
    profile =user_profile.objects.get(id = id)
    profile.delete()
    return redirect('profiletable')

def profiletable(request):
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    profiles = user_profile.objects.all()
    return render(request, 'cadmin/Users/profiletable.html' , {'profiles':profiles,'profile':profile,'notification':notification})

def edit_profile(request ,id):
    user = user_profile.objects.get(id =id)
    if request.method == "POST":
        user.ur_landmark = request.POST.get('ur_landmark')
        user.ur_locality = request.POST.get('ur_locality')
        user.ur_city = request.POST.get('ur_city')
        user.ur_state = request.POST.get('ur_state')
        user.ur_country = request.POST.get('ur_country')
        user.ur_pin = request.POST.get('ur_pin')
        user.ur_phone = request.POST.get('ur_phone')
        user.ur_DOB = request.POST.get('ur_DOB')
        user.ur_bio = request.POST.get('ur_bio')
        if 'ur_pic' in request.FILES and request.FILES['ur_pic'].size > 0:
            user.ur_pic = request.FILES['ur_pic']
        elif 'old' in request.POST and request.POST['old']:
            user.ur_pic = request.POST['old']
        user.save()
        return redirect('profiletable')
    return render(request , 'cadmin/Users/edit_profile.html' , {'profile':user})

def jobtable(request):
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    jobs = JobPortal.objects.all()
    return render(request, 'cadmin/Users/jobtable.html' , {'jobs':jobs,'profile':profile,'notification':notification})

def jobedit(request,id):
    Job =JobPortal.objects.get(id = id)
    if request.method == 'POST':
        Job.job_title = request.POST['jobtitle'].strip()
        Job.company_name = request.POST['companyname'].strip()
        Job.job_location = request.POST['location'].strip()
        Job.job_category = request.POST['job-category']
        Job.job_package = request.POST['package']
        Job.job_type = request.POST['job-type']
        Job.job_deadline = request.POST['deadline']
        Job.job_description = request.POST['jobdescription'].strip()
        Job.save()
        return redirect('jobtable')
    return render(request,'cadmin/Users/jobedit.html',{"job":Job})


def deletejob(request,id):
    job =JobPortal.objects.get(id = id)
    job.delete()
    return redirect('jobtable')

def posttable(request):
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    posts = user_posts.objects.all()
    return render(request, 'cadmin/Users/post_table.html' , {'posts':posts,'profile':profile,'notification':notification})

def post_status(request,id):
    post =user_posts.objects.get(id = id)
    if post.pt_status == True:
        post.pt_status = False
        post.save()
    else:
        post.pt_status =True
        post.save()
    return redirect('posttable')


def liketable(request):
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    likes = post_likes.objects.all()
    return render(request,'cadmin/Users/liketable.html',{'likes':likes,'profile':profile,'notification':notification})


def likestatus(request,id):
    liked =post_likes.objects.get(id = id)
    if liked.like == True:
        liked.like = False
        liked.save()
    else:
        liked.like =True
        liked.save()
    return redirect('liketable')

def comment_table(request):
    notification = Notifications.objects.filter(noti_status=True)
    profile = user_profile.objects.get(user=request.user)
    comment = post_comments.objects.all()
    return render(request,'cadmin/Users/comment_table.html',{'comments':comment,'profile':profile,'notification':notification})


def deletecomment(request,id):
    comment =comment_table.objects.get(id = id)
    comment.delete()
    return redirect('commenttable')



def profileadd(request):
    profile = user_profile.objects.get(user=request.user)
    if request.method == "POST":
        username = request.POST['username']
        users =User.objects.all()
        value = False
        for i in users:
            if i.username == username:
                value = True
                break
        if value == True :
            user = User.objects.get(username=username)
            Landmark = request.POST['Landmark']
            Locality = request.POST['Locality']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            pin = request.POST['pin']
            Phone = request.POST['Phone']
            Birthday = request.POST['Birthday']
            bio = request.POST['bio']
            image = request.FILES['image']
            user_create = user_profile(ur_pic=image, user=user, ur_landmark=Landmark, ur_locality=Locality,
                                    ur_city=city, ur_state=state, ur_country=country, ur_pin=pin, ur_phone=Phone,
                                    ur_DOB=Birthday, ur_bio=bio)
            user_create.save()
            return redirect('profiletable')
        else:
            msg = 'user does not exist! create user first...'
            return render(request, 'cadmin/Users/profileadd.html',{'profile':profile,'msg':msg})

    
    return render(request, 'cadmin/Users/profileadd.html',{'profile':profile})


def adduser(request):
    profile = user_profile.objects.get(user=request.user)
    if request.method == "POST":
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            msg = 'user already exists!....'
            return render(request,'cadmin/Users/useradd.html',{'profile':profile,'msg':msg})
        else:
            FirstName =request.POST['FirstName']
            LastName =request.POST['LastName']
            password =request.POST['password']
            Email =request.POST['Email']
            new = User(username=username,password=password,last_name=LastName,first_name=FirstName,is_superuser=False,is_active=True,is_staff=False,email=Email)
            new.save()
            return redirect('table')
    return render(request,'cadmin/Users/useradd.html',{'profile':profile})


def follow_bridge(request):
    follow = user_follow.objects.all()
    profile = user_profile.objects.get(user=request.user)
    return render(request,"cadmin/Users/Follow_bridge.html",{"follow":follow,"profile":profile})

def unfollow(request,id):
    follows = user_follow.objects.get(id=id)
    if follows.follow_status == True:
        follows.follow_status = False
    else:
        follows.follow_status = True
    follows.save()
    return redirect('follow_bridge')

def msg_table(request):
    profile = user_profile.objects.get(user=request.user)
    msg = messages.objects.all()
    return render(request,'cadmin/Users/message_table.html',{"msg":msg,"profile":profile})



def msg_delete(request,id):
    msg = messages.objects.get(id=id)
    msg.delete()
    return redirect('msg_table')

def admin_msg(request):
    adminmsg = admin_messages.objects.all()
    profile = user_profile.objects.get(user=request.user)
    return render(request,'cadmin/Users/Admin_msg.html',{'msgs':adminmsg,'profile':profile})

def solve(request,id):
    adminmsg = admin_messages.objects.get(id=id)
    if adminmsg.msg_status == True:
       adminmsg.msg_status = False
    else:
         adminmsg.msg_status = True
    adminmsg.save()
    return redirect('admin_msg')




