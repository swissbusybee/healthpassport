from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils import timezone
from datetime import datetime

class FamilyGroup(models.Model):
    family_group_name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('familygroup-detail', args=[str(self.id)])

    def __str__(self):
        return self.family_group_name

class Vaccine(models.Model):
    AGE_CHOICES = [('0-1 yrs', '0-1 yrs'),('1-5 yrs', '1-5 yrs'),('6-10 yrs', '6-10 yrs'),('Any Age', 'Any Age')]
    COUNTRY_CHOICES = [('Tanzania', 'Tanzania'),('Ghana', 'Ghana'),('Mexico', 'Mexico'),('Switzerland', 'Switzerland')]
    DISEASE_TYPE_CHOICES = [('Diptheria', 'Diptheria'),('Hepatitis B', 'Hepatitis B'),('Haemophilus influenzae type b', 'Haemophilus influenzae type b'),('Human papillomavirus', 'Human papillomavirus'), ('Seasonal influenza', 'Seasonal influenza'), ('Measles', 'Measles'), ('Mumps', 'Mumps'), ('Pertussis (Whooping Cough)', 'Pertussis (Whooping Cough)'), ('Rubella', 'Rubella'), ('Pneumococcal disease', 'Pneumococcal disease'), ('Poliomyelitis (Polio)', 'Poliomyelitis (Polio)'), ('Rotavirus', 'Rotavirus'), ('Tetanus', 'Tetanus'), ('Tuberculosis (TB)', 'Tuberculosis (TB)'), ('Varicella', 'Varicella')] 
    vaccine_name = models.CharField(max_length=200)
    disease_type = models.CharField(max_length=200, choices=DISEASE_TYPE_CHOICES, blank=True)
    required_doses = models.CharField(max_length=200)
    required_country = models.CharField(max_length=200, choices=COUNTRY_CHOICES, blank=True)
    recommended_age = models.CharField(max_length=200, choices=AGE_CHOICES, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vaccine-detail', args=[str(self.id)])

    def __str__(self):
        return self.vaccine_name

class Profile(models.Model):
    CHOICES = [('Parent', 'Parent'),('Child', 'Child'),('Other', 'Other')]
    BLOOD_TYPE_CHOICES = [('A RhD positive A+', 'A RhD positive A+'),('A RhD negative A-', 'A RhD negative A-'),('B RhD positive B+', 'B RhD positive B+'), ('B RhD negative B-', 'B RhD negative B-'), ('O RhD positive O+', 'O RhD positive O+'), ('O RhD negative O-', 'O RhD negative O-' ), ('AB RhD positive AB+', 'AB RhD positive AB+'), ('AB RhD negative AB-', 'AB RhD negative AB-')]
    familygroup = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(default=None)
    phone_number = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200, blank=True)
    doctor_name_contact = models.CharField(max_length=200, blank=True)
    blood_type = models.CharField(max_length=500, choices=BLOOD_TYPE_CHOICES, blank=True)
    allergies = models.CharField(max_length=200, blank=True)
    existing_health_conditions = models.CharField(max_length=200, blank=True)
    family_member_type = models.CharField(max_length=200, choices=CHOICES, blank=True)
    vaccine_card_image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name

class Immunization(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, blank=True, null=True) 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)    
    expired_by = models.DateField(null=True, blank=True)
    date_administered = models.DateField(null=True, blank=True)
    administered_by = models.CharField(max_length=200, blank=True)
    certified_by = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('immunization-detail', args=[str(self.id)])

    def __str__(self):
        return self.vaccine.vaccine_name 

    def vaccine_expired(self):
        return self.expired_by < datetime.now().date()

    

