from django.shortcuts import render, HttpResponse

# Create your views here.

# ----------------------------------------------------------------------------------------------|
# initial server response

def index (request):
    return HttpResponse ('This is a test!')
