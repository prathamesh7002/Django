from django.shortcuts import render, redirect
from django.http import HttpResponse
from form.forms import RegisterForm
from .models import Register

def view_form(request):
     Reg_form = RegisterForm()
     return render(request, 'form.html',{'form':Reg_form})

def submit_user(request):
     if request.method == "POST":
          username=request.POST.get('username'),
          email=request.POST.get('email'),
          password=request.POST.get('password'),
          confirm_password=request.POST.get('confirm_password'),
          first_name=request.POST.get('first_name'),
          last_name=request.POST.get('last_name'),
          phone_number=request.POST.get('phone_no'),
     
          new_user=Register(
               username=username,
               email=email,
               password=password,
               confirm_password=confirm_password,
               first_name=first_name,
               last_name=last_name,
               phone_number=phone_number)
          new_user.save()

          return HttpResponse("New user register successfully!")
     return HttpResponse("Invalid request Method")