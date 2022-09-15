from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# ------------------------------------------------------------
# How to render a template using views
# def index(request):
#     return render(request, "index.html")

# ------------------------------------------------------------

# passing a dictionary to the template using context
def index(request):
    context = {
        "name":"Veries",
        "favorite_color":"Blue",
        "pets": ["Remy", "Tiger", "Lil Dirt"]
        
    }
    return render(request,"index.html", context)
# ------------------------------------------------------------
