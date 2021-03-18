from django.shortcuts import render, HttpResponse

# Create your views here.

# ----------------------------------------------------------------------------------------------|
# Create method for page for the survey form

def index (request):
    return render(request, 'survey.html')

# ----------------------------------------------------------------------------------------------|
# Create method to process the request page for the survey form

def process (request):
    # Conditional
    if request.method == 'POST':
        # context handles key value pair (Dictionary)
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')

