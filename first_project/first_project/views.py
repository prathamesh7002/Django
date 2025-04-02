from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader
import mysql.connector
from .models import user

def hello(request):
 return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def date(request):
  now = datetime.datetime.now()
  html1 = "<html><body><h3>Now time is %s.</h3></body></html>" % now
  return HttpResponse(html1) 

def login(request):
    return render(request, 'login.html')  

def forget(request):
 template2 = loader.get_template('forget.html')
 return HttpResponse(template2.render()) 

def signin(request):
 template3 = loader.get_template('signin.html')
 return HttpResponse(template3.render()) 

def submit_user(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        language=request.POST.get('language')
        
        new_user=user(username=username,password=password,email=email,language=language)  # Create a new user instance
        new_user.save()
        
        return HttpResponse("User data submitted successfully!")
    return HttpResponse("Invalid request method.")

def view_users(request):
    users = user.objects.all()  # Fetch all users from the database
    return render(request, 'view.html', {'users': users})

from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie has been set successfully!")
    response.set_cookie('username', 'Prathamesh', max_age=3600)  # Cookie expires in 1 hour
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')  # Fetch cookie, default 'Guest' if not found
    return HttpResponse(f"Username from Cookie: {username}")

def delete_cookie(request):
    response = HttpResponse("Cookie has been deleted successfully!")
    response.delete_cookie('username')  # Deletes the 'username' cookie
    return response
