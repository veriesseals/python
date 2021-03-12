from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# Functions or Methods

# ---------------------------------------------------------------------------|
# Create a method called index

def index (request):
    # display string "Placeholder to later display a list of all blogs" by using return 
    return HttpResponse ("Placeholder to later display a list of all blogs")

# ---------------------------------------------------------------------------|
# Create a Function or Method called new

def new (request):
    # display string "Placeholder to display a new form to create a new blog" by using return
    return HttpResponse ("Placeholder to display a new form to create a new blog")

# ---------------------------------------------------------------------------|
# Create a Function or Method called create
def create (request):
    return redirect('/')

# ---------------------------------------------------------------------------|
# Create a Function or Method called show
def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

# ---------------------------------------------------------------------------|
# Create a Function or Method called edit
def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

# ---------------------------------------------------------------------------|
# Create a Function or Method called destroy
def destroy(request, number):
    return redirect('/')


# Templates
# ---------------------------------------------------------------------------|
# Create a Function or Method called destroy


