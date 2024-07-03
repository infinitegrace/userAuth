from django.shortcuts import render
from . models import Feature
# Create your views here.
def index(request):
  feature1 = Feature()
  feature1.id = 0
  feature1.name = 'franklin'
  feature1.details = "Has been tested and trusted "
  feature1.is_true = True
  
  feature2 = Feature()
  feature2.id = 1
  feature2.name = 'Uche'
  feature2.details = 'Very afordable'
  feature2.is_true = False
  
  features = [feature1,feature2]
  return render(request, 'index.html',{'feature':features})