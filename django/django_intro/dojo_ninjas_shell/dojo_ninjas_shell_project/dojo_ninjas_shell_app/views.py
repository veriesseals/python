from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# -------------------------------------------------------------|
# initial method

def index (request):
    return HttpResponse ("Glory, Glory!")
