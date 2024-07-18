from django.shortcuts import render
from . models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.http import HttpResponse

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
  
def login(request):
  if request.method == 'POST':
    return HttpResponse("<h1>You have successfully logged in</h1>")
  
  return render(request, 'login.html')
 
def register(request):
  if request.method == 'POST':
    username = request.POST('username')
    email = request.POST('email')
    password1 = request.POST('password1')
    password2 = request.POST('password2')
    
    if password1 == password2:
      if User.objects.filter(email = email).exists():
        messages.info(request, 'Email Aready Used')
        return redirect ('register')
        
      elif User.objects.filter(username = username).exists():
        messages.info(request, 'Username already in use')
        return redirect ('register')
        
      else:
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
  else:
    return render (request, 'register.html')
       
    
      
      
      
      
  
  return render(request, 'register.html')