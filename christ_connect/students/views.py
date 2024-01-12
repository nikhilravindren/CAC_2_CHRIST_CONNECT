from django.shortcuts import render,redirect
from .models import JobPortal
from cadmin.models import user_profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required


def user_user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user is not None and user.is_active:
            if user.is_superuser == False and user.is_staff == False:
                login(request , user)
                return redirect('home')
            elif user.is_superuser == False and user.is_staff == True:
                login(request , user)
                return redirect('home')
            else:
                msg = "You are not autherized for the access!"
                return render(request , 'cadmin/Users/login.html' , {'msg':msg})
        else:
            msg = "Wrong credentials"
            return render(request , 'cadmin/Users/login.html' , {"msg":msg})
    return render(request , 'cadmin/Users/login.html')

def job(request):
    datas =JobPortal.objects.all()
    fdata =JobPortal.objects.filter(job_type="full-time")
    pdata= JobPortal.objects.filter(job_type="part-time")
    udata = JobPortal.objects.values("job_category").distinct()
    ldata = JobPortal.objects.values("job_location").distinct() 
    mdata = JobPortal.objects.values("job_package").distinct()
    datas =list(datas)
    fdata =list(fdata)
    pdata =list(pdata)
    datas.reverse()
    fdata.reverse()
    pdata.reverse()
    a=datas[:5]
    B=fdata[:5]
    C=pdata[:5]
    mcount =JobPortal.objects.filter(job_category="Marketing").count()
    ccount =JobPortal.objects.filter(job_category="customer Service").count()
    hcount =JobPortal.objects.filter(job_category="Human Resource").count()
    pcount =JobPortal.objects.filter(job_category="Project Management").count()
    bcount =JobPortal.objects.filter(job_category="Business Development").count()
    scount =JobPortal.objects.filter(job_category="Sales and Communication").count()
    tcount =JobPortal.objects.filter(job_category="Teaching and Education").count()
    dcount =JobPortal.objects.filter(job_category="Design and Creative").count()

    return render(request,'student\index.html',{"datas":a,"jobs":B,"pjobs":C,"fdata":udata,"ldata":ldata,"mdata":mdata,"mcount":mcount,
                                                 "ccount":ccount,"hcount":hcount,"pcount":pcount,"bcount":bcount,"scount":scount,"tcount":tcount,"dcount":dcount,})

def jobposting(request):
    if request.POST:
        user = request.user
        job_title =request.POST['jobtitle'].strip()
        company_name=request.POST['companyname'].strip()
        location=request.POST['location'].strip()
        job_category=request.POST['job-category']
        package=request.POST['package']
        job_type=request.POST['job-type']
        deadline=request.POST['deadline']
        jobdescription=request.POST['jobdescription'].strip()
        data =JobPortal(user=user ,job_title=job_title,company_name=company_name,job_location=location,job_category=job_category,job_package=package,job_type=job_type,job_deadline=deadline,job_description=jobdescription)
        data.save()
        msg = "thank you for add job!"
        return render(request,'student\jobposting.html',{"msg":msg})
    return render(request,'student\jobposting.html')

def jobsearch(request):
    if request.POST:
        spackage =request.POST['spackage']
        slocation =request.POST['slocation']
        if spackage == ' ':
            jobs =JobPortal.objects.filter(job_location=slocation)
        elif slocation == ' ':
            jobs =JobPortal.objects.filter(job_package=spackage)
        else:
            jobs =JobPortal.objects.filter(job_package=spackage,job_location=slocation)
        return render(request,'student\jobsearch.html',{"datas":jobs})

def jobcategory(request,id):
    job =JobPortal.objects.filter(job_category=id)
    return render(request,'student\jobsearch.html',{"datas":job})

def details(request,id):
    job =JobPortal.objects.get(id =id)
    return render(request,'student\details.html',{"data":job})


def fulljob(request):
    all_datas =JobPortal.objects.all()
    paginator = Paginator(all_datas, 10)  # Show 10 datas per page

    page = request.GET.get('page')
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    return render(request,'student\Fulljobs.html',{"datas":datas})


#user profile 

def home(request):
    try:
        userprofile = user_profile.objects.get(user=request.user)

        return render(request, 'user/home.html', {'user_profile': userprofile, 'profile_exists': True})
    except user_profile.DoesNotExist:
        return render(request, 'user/home.html', {'profile_exists': False})
    

def editprofile(request):
    user = request.user
    username = user.username
    data=user_profile.objects.get(user=request.user)
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    return render(request,"user/profiledit.html",{"data":data,'user': user, 'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})


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
        user_create = user_profile(ur_pic=image,user=request.user,ur_landmark=Landmark,ur_locality=Locality,ur_city=city,ur_state=state,ur_country=country,ur_pin=pin,ur_phone=Phone,ur_DOB=Birthday,ur_bio=bio)
        user_create.save()
        return redirect('home')
    
    return render(request,'user/addprofile.html')        












