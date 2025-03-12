from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import *
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    return render(request, "index.html")

def services(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "services.html")

def contact(request, id=None):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    if request.method == "POST":
        # id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        
        if id is None:
            # Create new contact
            contact = Contact(name=name, email=email, desc=desc, phone=phone, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
        else:
            # Update existing contact
            contact = Contact.objects.get(id = id)
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.desc = desc
            contact.date = datetime.today()  # Optional: Update the date if needed
            contact.save()
            messages.success(request, "Your message has been updated successfully!")
            return redirect("/contact")

    context = {}
    if id is not None:
        queryset = Contact.objects.get(id = id)
        context = {'contactDetail' : queryset}

    return render(request, "contact.html", context)

def contactList(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    queryset = Contact.objects.all()
    

    search_query = request.GET.get("search")
    if search_query:
        queryset = Contact.objects.filter(name__icontains=search_query) | Contact.objects.filter(email__icontains=search_query) | Contact.objects.filter(phone__icontains=search_query) | Contact.objects.filter(desc__icontains=search_query) 

    context={'contactList' : queryset}
    return render(request, "contactList.html", context)

def delete_contactList(request,id):
    if(int(id) > 0):
        queryset = Contact.objects.get(id=int(id))
        queryset.delete()
    return redirect("/contactList")

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

