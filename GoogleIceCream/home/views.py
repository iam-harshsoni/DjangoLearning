from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.
def index(request):

    context = {
        'variable' : "this is sent by harsh",
        'variable1' : "this is sent by nakul"
    }

    # return HttpResponse("This is Home Page")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, "services.html")


@login_required(login_url="/login/") #can use this login_required decorator 
def contact(request):

    # if not request.user.is_authenticated:
    #     return redirect("/login/")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())

        contact.save()
        messages.success(request, "Your contact request has been sent successfully!.")
    return render(request, "contact.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Username does not exists.")
            return redirect('/login/')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Invalid Username or Password.")
            return render(request, "login.html")

    return render(request, "login.html")

def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password=request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            username = username,
            email = email,
            # password = password,
        )

        user.set_password(password)  # this method is use to encrypt the password.
        user.save()
        return redirect('/login/')

    return render(request, "register.html")

def logoutUser(request):
    logout(request)
    return redirect("/login/")