from django.shortcuts import render
from .forms import FileUploadForm
from django.http import HttpResponse

def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})



def set_session(request):
    request.session['username'] = 'Prathamesh'
    request.session['user_id'] = 101
    return HttpResponse("Session Data Set Successfully!")

def get_session(request):
    username = request.session.get('username', 'Guest')
    user_id = request.session.get('user_id', 'Unknown')
    return HttpResponse(f"Username: {username}, User ID: {user_id}")


