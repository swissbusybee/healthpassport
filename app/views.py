from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def vaccines(request):
    return render(request, 'app/vaccines.html')

def manage(request):
    return render(request, 'app/manage.html')