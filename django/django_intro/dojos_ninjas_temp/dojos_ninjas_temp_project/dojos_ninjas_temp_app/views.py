from django.shortcuts import render, HttpResponse, redirect
from dojos_ninjas_temp_app.models import Dojo, Ninja

# Create your views here.

# ---------------------------------------------------------|
# intial method with context

def index (request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

# ---------------------------------------------------------|
# create method

def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo_id=request.POST['dojo'],
    )
    return redirect('/')

# ---------------------------------------------------------|
# delete method
