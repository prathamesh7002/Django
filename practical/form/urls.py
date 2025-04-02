from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.view_form),
    path('submit-user/', views.submit_user, name='submit_user'),
]

