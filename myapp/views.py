from django.shortcuts import render
from . models import Feature
# Create your views here.
def index(request):
  
  features = Feature.objects.all
  return render(request, 'index.html',{'feature':features})

def contact(request):
  return render(request, 'contact.html')


def properties(request):
  return render(request, 'properties.html')


def property_details(request):
  return render(request, 'properties-details.html')