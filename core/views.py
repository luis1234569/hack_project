from django.shortcuts import render

# Create your views here.
def base (request):
    return render(request, 'base.html')

def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')
