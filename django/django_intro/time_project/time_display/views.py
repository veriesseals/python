from django.shortcuts import render, HttpResponse
from time import gmtime, strftime # importing current time

# Create your views here.

# -------------------------------------------------------------------------|
# Initial test method
# def index (request):
#     return HttpResponse("This is my Response!")

# -------------------------------------------------------------------------|
# run a method in your controller file (views.py) that renders a template displaying the current date and time.
# Time Method

def index (request):
    context = {
        "time": strftime("%m-%d-%Y %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)


