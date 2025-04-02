from django.urls import path
from . import views
from django.urls import path
from .views import set_session, get_session



urlpatterns = [
    path('', views.upload_file, name='upload_file'),  # Example view
    path('set/', views.set_session, name='set_session'),
    path('get/', views.get_session, name='get_session'),
]