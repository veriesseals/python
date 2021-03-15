from django.shortcuts import render, HttpResponse, redirect

# ------------------------------------------------------------------|
# Create your views here.

# ------------------------------------------------------------------|
# Intial Test Method
def index (request):
    return HttpResponse ("This is my response!")

# ------------------------------------------------------------------|
# Create Get and Post Methods

def some_function (request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "some_template.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return redirect("/")


# To access the form data from a POST request, we can refer to request.POST - 
# a python dictionary containing key-value-pairs for each input submitted from the form. 
# (If the form is a GET request, that data can be accessed with request.GET.)

# ------------------------------------------------------------------|
# Create request.POST and request.GET to access the form data from a POST request and Get request.

def some_function (request):
    if request.method == "GET":
        print (request.GET)
    if request.method == "POST":
        print (request.POST)
        
def some_function (request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        
    