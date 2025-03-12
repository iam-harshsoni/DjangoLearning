from django.db import models
from django.contrib.auth.models import User


"""
makemigrations = create changes and store them in a file
migrations = apply the pending changes created by makemigrations
""" 

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    contact_ran_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.email}"
        
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta():
        ordering = ['department']

class StudentID(models.Model):
    studentId = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.studentId
    
    class Meta():
        ordering = ['studentId']

class Student(models.Model):
    department = models.ForeignKey(Department,related_name="depart", on_delete=models.CASCADE)
    
    # One to one Relation
    student_id = models.OneToOneField(StudentID, related_name="studentID", on_delete=models.CASCADE)

    # One to Many Relation using ForeignKey
    # student_id = models.ForeignKey(StudentID, related_name="students", on_delete=models.CASCADE, default=1)
    
    # Many to Many Realtion
    # student_id = models.ManyToManyField(StudentID, related_name="studentID")
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta():
        ordering = ['student_name']
        verbose_name = "student"
