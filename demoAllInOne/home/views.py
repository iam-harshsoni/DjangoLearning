from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    return render(request, "index.html")

def services(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "services.html")

def contact(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, desc=desc, phone=phone, date=datetime.today())

        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request, "contact.html")

def about(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    return render(request, "about.html")

def loginUser(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        # else:
        #     # No backend authenticated the credentials
        #      return render(request, "login.html")
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

