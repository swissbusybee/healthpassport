from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
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

class FamilyGroupCreate(CreateView):
    model = FamilyGroup
    template_name_suffix = '_create_form'
    fields = ['family_group_name']

class FamilyGroupUpdate(UpdateView):
    model = FamilyGroup
    template_name_suffix = '_update_form'
    fields = ['family_group_name']

class FamilyGroupDelete(DeleteView):
    model = FamilyGroup
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('familygroups')

class ProfileListView(generic.ListView):
    model = Profile

class ProfileDetailView(generic.DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    template_name_suffix = '_create_form'
    fields = ['familygroup','first_name', 'last_name', 'date_of_birth', 'phone_number', 'emergency_contact', 'doctor_name_contact', 'blood_type', 'allergies', 'existing_health_conditions', 'family_member_type']

class ProfileUpdate(UpdateView):
    model = Profile
    template_name_suffix = '_update_form'
    fields = ['familygroup','first_name', 'last_name', 'date_of_birth', 'phone_number', 'emergency_contact', 'doctor_name_contact', 'blood_type', 'allergies', 'existing_health_conditions', 'family_member_type']

class ProfileDelete(DeleteView):
    model = Profile
    template_name_suffix = '_delete_form'
    success_url = "/familygroup/{familygroup_id}"

class VaccineListView(generic.ListView):
    model = Vaccine

class VaccineDetailView(generic.DetailView):
    model = Vaccine

class VaccineCreate(CreateView):
    model = Vaccine
    template_name_suffix = '_create_form'
    fields = ['vaccine_name', 'disease_type', 'required_doses', 'required_country', 'recommended_age', 'notes']

class VaccineUpdate(UpdateView):
    model = Vaccine
    template_name_suffix = '_update_form'
    fields = ['vaccine_name', 'disease_type', 'required_doses', 'required_country', 'recommended_age', 'notes']

class VaccineDelete(DeleteView):
    model = Vaccine
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('vaccines')

class ImmunizationListView(generic.ListView):
    model = Immunization

class ImmunizationDetailView(generic.DetailView):
    model = Immunization
 
class ImmunizationCreate(CreateView):
    model = Immunization
    template_name_suffix = '_create_form'
    fields = ['vaccine', 'profile', 'expired_by', 'date_administered', 'administered_by', 'certified_by']

class ImmunizationUpdate(UpdateView):
    model = Immunization
    template_name_suffix = '_update_form'
    fields = ['vaccine', 'profile', 'expired_by', 'date_administered', 'administered_by', 'certified_by']

class ImmunizationDelete(DeleteView):
    model = Immunization
    template_name_suffix = '_delete_form'
    success_url = "/profile/{profile_id}"