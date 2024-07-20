from django.shortcuts import render, redirect
from . models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms

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
# uncomment this if you want to use the reinvented wheel
  # if request.method == 'POST':
  #   username = request.POST['username']
  #   email = request.POST['email']
  #   password1 = request.POST['password1']
  #   password2 = request.POST['password2']
    
  #   if password1 == password2:
  #     if User.objects.filter(email = email).exists():
  #       messages.info(request, 'Email Aready Used')
  #       return redirect ('/register/')
        
  #     elif User.objects.filter(username = username).exists():
  #       messages.info(request, 'Username already in use')
  #       return redirect ('/register/')
        
  #     else:
  #       user = User.objects.create_user(username=username, email=email, password=password1)
  #       user.save()
  #       return redirect('/log in/')

  #   else:
  #     messages.info(request,'Inconsistent Password') 
  #     return redirect ( '/register/')      
  # else:
  #   return render (request, 'register.html')      

  # Using the usercreation module to create and validate our form

# comment this session if the above session is uncommented
  
  
  class UserRegisterationForm(UserCreationForm):
    Email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
  form = UserRegisterationForm()

  return render(request, 'register.html', {'form':form})