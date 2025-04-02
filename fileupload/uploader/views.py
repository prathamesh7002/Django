from django.shortcuts import render
from .forms import FileUploadForm

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
    return render(request, 'session_set.html')

def get_session(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'session_get.html', {'username': username})

from django.shortcuts import render

def set_session(request):
    request.session['username'] = 'Prathamesh'
    return render(request, 'session_set.html')

def get_session(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'session_get.html', {'username': username})
