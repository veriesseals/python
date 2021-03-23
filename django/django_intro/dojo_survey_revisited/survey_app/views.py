from django.shortcuts import render, HttpResponse, redirect

LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Java'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'Online'
)

# Create your views here.

# ----------------------------------------------------------------------------------------------|
# Create method for page for the survey form

def index (request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'survey.html', context)

# ----------------------------------------------------------------------------------------------|
# Create method to process the request page for the survey form

def survey (request):
    # Conditional
    if request.method == 'GET':
        return redirect('/')
    
    request.session['result'] = {
        'name': request.POST['name'],
        'language': request.POST['language'],
        'location': request.POST['location'],
        'comment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)

