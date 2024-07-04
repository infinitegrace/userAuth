from django.urls import path
from . import views

urlpatterns =[
  path('',views.index, name = 'home'),
  path('properties/',views.properties, name = 'properties'),
  path('property-details',views.property_details, name = 'property_details'),

  path('contact/', views.contact, name = 'contact')
  ]