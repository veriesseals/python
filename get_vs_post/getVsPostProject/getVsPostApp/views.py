from django.http.response import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
# --------------------------------------------------------------------

def some_template(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "some_template.html")
    if request.method == "POST":
        print ("a POST request is being made to this route")
        return redirect("/")

# --------------------------------------------------------------------