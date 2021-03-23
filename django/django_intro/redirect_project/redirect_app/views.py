from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# -------------------------------------------------------------------|
# Initial Test Method

# -------------------------------------------------------------------|
# Initial Test Method Wrong way, without redirecting the page
# from django.shortcuts import render
    
# def create_user(request):
# 	print("Got POST data!")
#     name = request.POST['name']
#     email = request.POST['email']
#     return render(request, 'index.html')

# -------------------------------------------------------------------|
# Initial Test Correct Way, redirecting the page
def index (request):
    print('got here from redirect!')
    return render(request, ('index.html'))

def create_user(request):
    print("Got POST data!")
    name = request.POST['name']
    email = request.POST['email']
    return redirect('/')	# changed this line!


# -------------------------------------------------------------------|
# Apply migrations by using python manage.py migrate
# Implement Session
def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

# -------------------------------------------------------------------|
# Notes on session

# Session Breakdown:
# request.session['key'] = 'value'
# Stores 'value' in request.session['key'].
# if 'key' in request.session
# Useful for testing if key is in request.session or not.
# {{ request.session.name }}
# Use dot notation . to access request.session keys from templates, square brackets [] aren’t allowed there.
# del request.session['key']
# Deletes a session key if it exists, throws a KeyError if it doesn’t.
# request.session.flush()
# Clears all data from session.
