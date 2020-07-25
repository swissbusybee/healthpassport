from django.contrib import admin

from .models import FamilyGroup, Profile, Vaccine, Immunization

class ImmunizationInline(admin.TabularInline):
    model = Immunization
    fields = ("expired_by", "date_administered", "administered_by", "certified_by",)
    fk_name = "profile"   

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "isParent", "isChild",)
    list_filter = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions",)
    search_fields = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "isParent", "isChild",)
    inlines = [ImmunizationInline]

class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ("first_name", "last_name",)
    fk_name = "familygroup"

@admin.register(FamilyGroup)
class FamilyGroupAdmin(admin.ModelAdmin):
    list_display = ("family_group_name",)
    search_fields = ("family_group_name",)
    inlines = [ProfileInline]

@admin.register(Immunization)
class ImmunizationAdmin(admin.ModelAdmin):
    list_display = ("expired_by", "date_administered", "administered_by", "certified_by",)
    list_filter = ("expired_by", "date_administered", "administered_by", "certified_by",)
    search_fields = ("expired_by", "date_administered", "administered_by", "certified_by",)

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ("vaccine_name", "required_doses", "required_country", "reccomended_age", "notes",)
    list_filter = ("vaccine_name", "required_doses", "required_country", "reccomended_age",)
    search_fields = ("vaccine_name", "required_doses", "required_country", "reccomended_age",)