from django.shortcuts import render,redirect
from .models import JobPortal

# Create your views here.
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
        job_title =request.POST['jobtitle'].strip()
        company_name=request.POST['companyname'].strip()
        location=request.POST['location'].strip()
        job_category=request.POST['job-category']
        package=request.POST['package']
        job_type=request.POST['job-type']
        deadline=request.POST['deadline']
        jobdescription=request.POST['jobdescription'].strip()
        data =JobPortal(job_title=job_title,company_name=company_name,job_location=location,job_category=job_category,job_package=package,job_type=job_type,job_deadline=deadline,job_description=jobdescription)
        data.save()
        return redirect('jobposting')
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
    job =JobPortal.objects.get(job_id=id)
    return render(request,'student\details.html',{"data":job})










