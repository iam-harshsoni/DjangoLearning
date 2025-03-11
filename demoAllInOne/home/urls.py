from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('contact/<id>',views.contact, name="contact"),
    path('contactList/',views.contactList, name="contactList"),
    path('delete_contactList/<id>/', views.delete_contactList, name="delete_contactList"),
    path('about/',views.about, name="about"),
    path('login/',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),
]
