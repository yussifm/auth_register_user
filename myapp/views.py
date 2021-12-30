from os import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages, auth




# Create your views here.

def index(request):
    return render(request=request, template_name='index.html')


def counter(request):
    text_all = request.POST["text"]
    text_size = len(text_all.split())
    return render(
        request=request,
        template_name="counter.html",
        context={'textSize': text_size}
    )

def mypage(request):
    return render(request=request, template_name="page.html")

def register_page(request):
  
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['passwordConfirm']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request= request, message="Email already exits")
                return redirect(to="register")
            elif User.objects.filter(username=username).exists():
                messages.info(request= request, message="Uesrname already exits")
                return redirect(to="register")
            else:
                userCre = User.objects.create(email=email,password= password, username = username)
                User.save(self=userCre)
                return redirect(to="page")
        else:
            messages.info(request=request, message="password doesn't match")
            return redirect(to="register")  
            
        
    else:
        return render(request=request, template_name="register.html")
