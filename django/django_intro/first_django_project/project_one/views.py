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
# Create a Function or Method for rendering templates render must be in the import

def index(request):
    return render(request, "index.html")

# When we call the render function, our first argument will always be request, 
# and the second argument will be a string indicating which html file to render.

# Passing data to the template via the render_template method. Rather than being able 
# to pass up any number of arguments, we can only pass a single dictionary whose keys 
# will be the variable names available on the template. For example:

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)


