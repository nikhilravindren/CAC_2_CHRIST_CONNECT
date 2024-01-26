from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPortal, user_posts, post_comments, post_likes,user_follow,messages
from cadmin.models import user_profile,admin_messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from cadmin.models import Notifications
from itertools import chain
from operator import attrgetter



# login view
def user_user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            if user.is_superuser == False and user.is_staff == False:
                login(request, user)
                return redirect('home')
            elif user.is_superuser == False and user.is_staff == True:
                login(request, user)
                return redirect('home')
            else:
                msg = "You are not autherized for the access!"
                return render(request, 'cadmin/Users/login.html', {'msg': msg})
        else:
            msg = "Wrong credentials"
            return render(request, 'cadmin/Users/login.html', {"msg": msg})
    return render(request, 'cadmin/Users/login.html')


# views for job portal
def job(request):
    datas = JobPortal.objects.all()
    fdata = JobPortal.objects.filter(job_type="full-time")
    pdata = JobPortal.objects.filter(job_type="part-time")
    udata = JobPortal.objects.values("job_category").distinct()
    ldata = JobPortal.objects.values("job_location").distinct()
    mdata = JobPortal.objects.values("job_package").distinct()
    datas = list(datas)
    fdata = list(fdata)
    pdata = list(pdata)
    datas.reverse()
    fdata.reverse()
    pdata.reverse()
    a = datas[:5]
    B = fdata[:5]
    C = pdata[:5]
    mcount = JobPortal.objects.filter(job_category="Marketing").count()
    ccount = JobPortal.objects.filter(job_category="customer Service").count()
    hcount = JobPortal.objects.filter(job_category="Human Resource").count()
    pcount = JobPortal.objects.filter(job_category="Project Management").count()
    bcount = JobPortal.objects.filter(job_category="Business Development").count()
    scount = JobPortal.objects.filter(job_category="Sales and Communication").count()
    tcount = JobPortal.objects.filter(job_category="Teaching and Education").count()
    dcount = JobPortal.objects.filter(job_category="Design and Creative").count()

    return render(request, 'student\index.html',
                  {"datas": a, "jobs": B, "pjobs": C, "fdata": udata, "ldata": ldata, "mdata": mdata, "mcount": mcount,
                   "ccount": ccount, "hcount": hcount, "pcount": pcount, "bcount": bcount, "scount": scount,
                   "tcount": tcount, "dcount": dcount, })


def jobposting(request):
    if request.POST:
        user = request.user
        job_title = request.POST['jobtitle'].strip()
        company_name = request.POST['companyname'].strip()
        location = request.POST['location'].strip()
        job_category = request.POST['job-category']
        package = request.POST['package']
        job_type = request.POST['job-type']
        deadline = request.POST['deadline']
        jobdescription = request.POST['jobdescription'].strip()
        data = JobPortal(user=user, job_title=job_title, company_name=company_name, job_location=location,
                         job_category=job_category, job_package=package, job_type=job_type, job_deadline=deadline,
                         job_description=jobdescription)
        data.save()
        msg = "thank you for add job!"
        notifi = "posted a new job!"
        Notifications.objects.create(user_id=request.user,noti_msg=notifi)
        return render(request, 'student\jobposting.html', {"msg": msg})
    return render(request, 'student\jobposting.html')


def jobsearch(request):
    if request.POST:
        spackage = request.POST['spackage']
        slocation = request.POST['slocation']
        if spackage == ' ':
            jobs = JobPortal.objects.filter(job_location=slocation)
        elif slocation == ' ':
            jobs = JobPortal.objects.filter(job_package=spackage)
        else:
            jobs = JobPortal.objects.filter(job_package=spackage, job_location=slocation)
        return render(request, 'student\jobsearch.html', {"datas": jobs})


def jobcategory(request, id):
    job = JobPortal.objects.filter(job_category=id)
    return render(request, 'student\jobsearch.html', {"datas": job})


def details(request, id):
    job = JobPortal.objects.get(id=id)
    return render(request, 'student\details.html', {"data": job})


def fulljob(request):
    all_datas = JobPortal.objects.all()
    paginator = Paginator(all_datas, 10)  # Show 10 datas per page

    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    return render(request, 'student\Fulljobs.html', {"datas": datas})

def applyjob(request,id):
    puser = get_object_or_404(User, id=id)
    contant = user_profile.objects.all()
    msg = 'contact on this number:'
    noti_user = request.user
    noti_msg = "applied for a job!"
    Notifications.objects.create(user_id=noti_user,noti_msg=noti_msg)
    return render(request,'student/jobapply.html',{'contact':contant,'msg':msg,'puser':puser})

def about(request):
    return render(request,'student\About.html')



# home view for users

def home(request):
    if user_profile.objects.filter(user=request.user):
        userprofile = user_profile.objects.get(user=request.user)
        profile = user_profile.objects.all()
        posts = user_posts.objects.all()
        likes = post_likes.objects.all()
        like = post_likes.objects.filter(liked_by=request.user,like = True).values("post")
        print(like)
        a =[]
        for i in like:
            a.append(i["post"])
        print(a)

        posts = list(posts)
        posts.reverse()
        return render(request, 'user/home.html',
                      {'user_profile': userprofile, 'profile': profile, 'profile_exists': True, 'posts': posts,
                       'like': a, 'likes': likes})
    else:
        profile = user_profile.objects.all()
        posts = user_posts.objects.all()
        likes = post_likes.objects.all()
        like = post_likes.objects.filter(liked_by=request.user,like = True).values("post")
        a =[]
        for i in like:
            a.append(i["post"])
        print(a)
        posts = list(posts)
        posts.reverse()
        return render(request, 'user/home.html',
                      {'profile': profile, 'profile_exists': False, 'posts': posts, 'like': a, 'likes': likes})


def editprofile(request):
    user = request.user
    username = user.username
    data = user_profile.objects.get(user=request.user)
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    return render(request, "user/profiledit.html",
                  {"data": data, 'user': user, 'username': username, 'email': email, 'first_name': first_name,
                   'last_name': last_name})


def addprofile(request):
    if request.method == "POST":
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
        user_create = user_profile(ur_pic=image, user=request.user, ur_landmark=Landmark, ur_locality=Locality,
                                   ur_city=city, ur_state=state, ur_country=country, ur_pin=pin, ur_phone=Phone,
                                   ur_DOB=Birthday, ur_bio=bio)
        user_create.save()
        user = request.user
        noti_msg = "created his profile!"
        Notifications.objects.create(user_id=user,noti_msg=noti_msg)
        return redirect('home')

    return render(request, 'user/addprofile.html')


# media posting views


def posts(request):
    if request.method == "POST":
        try:
            pt_content = request.POST['content']
            pt_media = request.FILES['mediapost']
            post = user_posts(user=request.user, pt_content=pt_content, pt_media=pt_media)
            post.save()
            user = request.user
            noti_msg = "posted something!"
            Notifications.objects.create(user_id=user,noti_msg=noti_msg)
            return redirect('home')
        except:
            pt_content = request.POST['content']
            post = user_posts(user=request.user, pt_content=pt_content)
            post.save()
            user = request.user
            noti_msg = "posted something!"
            Notifications.objects.create(user_id=user,noti_msg=noti_msg)
            return redirect('home')





def like_post(request,id):
    post = user_posts.objects.get(id=id)
    likes = post_likes.objects.filter(post=post,liked_by=request.user)
    if likes:
        for like1 in likes:
            if like1.like == True:
                like1.like = False
                like1.save()
                post = user_posts.objects.get(id=id)
                post.pt_likes = post.pt_likes - 1
                post.save()
            else:
                like1.like =True
                like1.save()
                post = user_posts.objects.get(id=id)
                post.pt_likes = post.pt_likes + 1
                post.save()
    else:
        post.pt_likes = post.pt_likes + 1
        post.save()
        like = post_likes(post=post,liked_by=request.user,like=True)
        like.save()

    return redirect('home')






def profile(request):
    return render(request, 'user/profile.html')


def comment(request, id):
    if request.method == "POST":
        pt_comment = request.POST['comment']
        post = user_posts.objects.get(id=id)
        comment = post_comments(comment_by=request.user, pt_comment=pt_comment, post=post)
        comment.save()
        post.pt_comment= post.pt_comment +1
        post.save()
        user = request.user
        noti_msg = "commented something!"
        Notifications.objects.create(user_id=user,noti_msg=noti_msg)
        return redirect('home')

def peoples(request):
    all_datas = user_profile.objects.all()
    follows = user_follow.objects.filter(followd_by=request.user, follow_status=True).values('followd_to')
    a=[]
    for follow in follows:
        a.append(follow["followd_to"])
    print(a)
    paginator = Paginator(all_datas, 10)

    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    return render(request, 'user/peoples.html', {'datas': datas, 'follows': a})

def followes(request, id):
    followd_to = get_object_or_404(User, id=id)
    following = user_follow.objects.filter(followd_by=request.user, followd_to=followd_to)

    if following.exists():
        for follow in following:
            follow.follow_status = not follow.follow_status
            follow.save()
    else:
        following = user_follow(followd_by=request.user, followd_to=followd_to, follow_status=True)
        following.save()

    return redirect('peoples')


def connections(request):
    all_datas = user_profile.objects.all()
    followes = user_follow.objects.values('followd_to').filter(followd_by=request.user,follow_status=True)
    paginator = Paginator(all_datas, 10)

    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    return render(request, 'user/connections.html', {'datas': datas,'follows':followes})

def user_message(request,id):
    message_to = User.objects.get(id=id)
    message1 = messages.objects.filter(message_by=request.user,message_to=message_to)
    message2 = messages.objects.filter(message_by=message_to,message_to=request.user)
    merged_messages = list(chain(message1, message2))
    sorted_messages = sorted(merged_messages, key=attrgetter('message_on'))
    return render(request,"user\message.html",{"message":sorted_messages,'message_to':message_to})


def send_message(request,id):
    if request.method == "POST":
        msg = request.POST['msg']
        message_to = User.objects.get(id=id)
        messages.objects.create(message_by=request.user,message_to=message_to,message=msg)
        return redirect('user_message',id=id)


def send_admin(request):
    if request.method == 'POST':
        msg = request.POST['a_msg']
        subject = request.POST['a_sub']
        admin_messages.objects.create(msg_from=request.user,msg_content=msg,msg_subject=subject)
        return redirect('job')


    




