from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def hacker(request):
    return render(request,"home.html")

def signin(request):
    
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get("email")
            pass1=request.POST.get("psw")
            re_pass1=request.POST.get("psw-repeat")

            if pass1==re_pass1:
                en=User.objects.create_user(username,email,pass1)
                en.save()
                return HttpResponseRedirect("login")
                
            elif pass1!=re_pass1:
                return HttpResponse('password did not match')
    except:
        pass   
    return render(request,"signup.html")
    

def login_in(request):
    if request.method=="POST":
        user=request.POST.get("username")
        passw=request.POST.get("password")
        myuser=authenticate(request,username=user,password=passw)
        print(user,passw)
        if myuser is not None:
            login(request,myuser)
            return redirect("home")
        else:
            return HttpResponse("invalid user or password")
        
    return render(request,'login_in.html')


