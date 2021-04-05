from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# ------------------------------------------------------------------------
# intitial method

def index (request):
    return HttpResponse("Glory, Glory!")