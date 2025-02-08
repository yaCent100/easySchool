from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'courses/home.html')

def cours(request):
    return render(request, 'courses/cours.html')