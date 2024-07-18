from django.urls import path
from . import views

urlpatterns =[
  path('',views.index, name = 'home'),
  path('index.html',views.index, name = 'home'),  
  path('properties',views.properties, name = 'properties'),
  path('property-details/',views.property_details, name = 'property_details'),

  path('contact/', views.contact, name = 'contact'),
  path('log in/', views.login, name ='log-in'),
  path('register/', views.register, name = 'register'),
  
  ]
  
 