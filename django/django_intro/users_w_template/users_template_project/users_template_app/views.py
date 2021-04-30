from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.

# -----------------------------------------------------------------|
# initial method

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    User.objects.create (
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/')
