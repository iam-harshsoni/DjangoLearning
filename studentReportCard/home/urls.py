from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('students/',views.get_students,name="students"),
    path('marks/<student_id>',views.get_marks,name="marks")
]
