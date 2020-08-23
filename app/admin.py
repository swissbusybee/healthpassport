import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
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
    list_display = ("id", "first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type", "created_at")
    list_filter = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type",)
    search_fields = ("first_name", "last_name", "date_of_birth", "phone_number", "emergency_contact", "doctor_name_contact", "blood_type", "allergies", "existing_health_conditions", "family_member_type",)
    inlines = [ImmunizationInline]
    change_list_template = 'admin/app/profile/change_list.html'
    ordering = ("-created_at",)

class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ("first_name", "last_name", "family_member_type")
    fk_name = "familygroup"

@admin.register(FamilyGroup)
class FamilyGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FamilyGroupResource
    list_display = ("id", "family_group_name",)
    search_fields = ("family_group_name",)
    inlines = [ProfileInline]

@admin.register(Immunization)
class ImmunizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ImmunizationResource
    list_display = ("id", "get_vaccine_name", "expired_by", "date_administered", "administered_by", "certified_by", "created_at")
    list_filter = ("vaccine", "expired_by", "date_administered", "administered_by", "certified_by",)
    search_fields = ("vaccine", "expired_by", "date_administered", "administered_by", "certified_by",)
    change_list_template = 'admin/app/immunization/change_list.html'
    ordering = ("-created_at",)

    def get_vaccine_name(self, obj):
        return obj.vaccine.vaccine_name
    get_vaccine_name.short_description = 'Vaccine Name'
    get_vaccine_name.admin_order_field = 'vaccine'  

        # Inject chart data on page load in the ChangeList view
    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Our custom urls have to go before the default urls, because they
        # default ones match anything.
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            Immunization.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

@admin.register(Vaccine)
class VaccineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VaccineResource
    list_display = ("id", "vaccine_name", "required_doses", "required_country", "recommended_age", "notes", "created_at")
    list_filter = ("vaccine_name", "required_doses", "required_country", "recommended_age",)
    search_fields = ("vaccine_name", "required_doses", "required_country", "recommended_age",)

    change_list_template = 'admin/app/vaccine/change_list.html'
    ordering = ("-created_at",)

    # Inject chart data on page load in the ChangeList view
    def changelist_view(self, request, extra_context=None):
        chart_data = self.chart_data()
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
        ]
        # NOTE! Our custom urls have to go before the default urls, because they
        # default ones match anything.
        return extra_urls + urls

    # JSON endpoint for generating chart data that is used for dynamic loading
    # via JS.
    def chart_data_endpoint(self, request):
        chart_data = self.chart_data()
        return JsonResponse(list(chart_data), safe=False)

    def chart_data(self):
        return (
            Vaccine.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

