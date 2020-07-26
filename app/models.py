from django.db import models
from django.urls import reverse

class FamilyGroup(models.Model):
    family_group_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('familygroup-detail', args=[str(self.id)])

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=200)
    disease_type = models.CharField(max_length=200)
    required_doses = models.CharField(max_length=200)
    required_country = models.CharField(max_length=200)
    reccomended_age = models.CharField(max_length=200)
    notes = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('vaccine-detail', args=[str(self.id)])

class Profile(models.Model):
    familygroup = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(default=None)
    phone_number = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200, blank=True)
    doctor_name_contact = models.CharField(max_length=200, blank=True)
    blood_type = models.CharField(max_length=500, blank=True)
    allergies = models.CharField(max_length=200, blank=True)
    existing_health_conditions = models.CharField(max_length=200, blank=True)
    isParent = models.BooleanField(default=False)
    isChild = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

class Immunization(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, default=None) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)    
    expired_by = models.DateField(null=True, blank=True)
    date_administered = models.DateField(null=True, blank=True)
    administered_by = models.CharField(max_length=200, blank=True)
    certified_by = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('immunization-detail', args=[str(self.id)])

    

