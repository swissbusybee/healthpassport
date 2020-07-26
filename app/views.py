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

# def manage(request):
#     all_family_groups = FamilyGroup.objects.all()
#     context = { 'all_family_groups': all_family_groups}
#     return render(request, 'app/manage.html', context)

# def family_group_detail(request, familygroup_id):
#     familygroup = FamilyGroup.objects.get(pk=familygroup_id)
#     all_profiles = Profile.objects.all()
#     context = {
#         'familygroup': familygroup,
#         'all_profiles': all_profiles,
#         }
#     return render(request, 'app/family_group_detail.html', context)

# def profile_detail(request, profile_id):
#     profile = get_object_or_404(Profile, pk=profile_id)
#     context = {
#         'profile': profile,
#         }
#     return render(request, 'app/profile_detail.html', context)

class FamilyGroupListView(generic.ListView):
    model = FamilyGroup

class FamilyGroupDetailView(generic.DetailView):
    model = FamilyGroup
  

class ProfileDetailView(generic.DetailView):
    model = Profile
 