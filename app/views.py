from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import FamilyGroup, Profile, Vaccine, Immunization

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class FamilyGroupListView(generic.ListView):
    model = FamilyGroup

class FamilyGroupDetailView(generic.DetailView):
    model = FamilyGroup
  
class ProfileDetailView(generic.DetailView):
    model = Profile

class VaccineListView(generic.ListView):
    model = Vaccine

class VaccineDetailView(generic.DetailView):
    model = Vaccine

class ImmunizationListView(generic.ListView):
    model = Immunization

class ImmunizationDetailView(generic.DetailView):
    model = Immunization
 