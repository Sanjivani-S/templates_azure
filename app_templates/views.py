from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def other(request):
    return render(request,'other.html')

def relative(request):
    return render (request, 'relative_url_templates.html')

def home(request):
    return render (request, 'home.html')

def details(request):
    return render(request, 'post_detail.html')
