from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required


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
    return render(request, 'cadmin/index.html')

def table(request):
    users = User.objects.all()
    return render(request, 'cadmin/Users/data-tables.html' , {'users':users})

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
    return render(request , 'cadmin/Users/edit_user.htm' , {'user':user})


