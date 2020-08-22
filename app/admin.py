from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import FamilyGroup, Profile, Vaccine, Immunization

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class VaccineResource(resources.ModelResource):
    class Meta:
        model = Vaccine

class ImmunizationResource(resources.ModelResource):
    class Meta:
        model = Immunization

class FamilyGroupResource(resources.ModelResource):
    class Meta:
        model = FamilyGroup

class ImmunizationInline(admin.TabularInline):
    model = Immunization
    fields = ("expired_by", "date_administered", "administered_by", "certified_by",)
    fk_name = "profile" 

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProfileResource
    list_display = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type",)
    list_filter = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type",)
    search_fields = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type",)
    inlines = [ImmunizationInline]
    change_list_template = 'admin/app/profile/change_list.html'

class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ("first_name", "last_name", "family_member_type")
    fk_name = "familygroup"

@admin.register(FamilyGroup)
class FamilyGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FamilyGroupResource
    list_display = ("family_group_name",)
    search_fields = ("family_group_name",)
    inlines = [ProfileInline]

@admin.register(Immunization)
class ImmunizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ImmunizationResource
    list_display = ("get_vaccine_name", "expired_by", "date_administered", "administered_by", "certified_by",)
    list_filter = ("vaccine", "expired_by", "date_administered", "administered_by", "certified_by",)
    search_fields = ("vaccine", "expired_by", "date_administered", "administered_by", "certified_by",)
    change_list_template = 'admin/app/immunization/change_list.html'

    def get_vaccine_name(self, obj):
        return obj.vaccine.vaccine_name
    get_vaccine_name.short_description = 'Vaccine Name'
    get_vaccine_name.admin_order_field = 'vaccine'  

@admin.register(Vaccine)
class VaccineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VaccineResource
    list_display = ("vaccine_name", "required_doses", "required_country", "recommended_age", "notes",)
    list_filter = ("vaccine_name", "required_doses", "required_country", "recommended_age",)
    search_fields = ("vaccine_name", "required_doses", "required_country", "recommended_age",)
    change_list_template = 'admin/app/vaccine/change_list.html'