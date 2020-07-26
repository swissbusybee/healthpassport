from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('familygroups/', views.FamilyGroupListView.as_view(), name='familygroups'),  
    path('familygroup/<int:pk>', views.FamilyGroupDetailView.as_view(), name='familygroup-detail'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),     
]