from django.db import models
from django.contrib.auth.models import User

"""
makemigrations = create changes and store them in a file
migrations = apply the pending changes created by makemigrations
""" 

# Create your models here.
        
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta():
        ordering = ['department']
        verbose_name = "Department"
        verbose_name_plural = "Departments"  # Custom plural name


class Subject(models.Model):
    subjectName = models.CharField(max_length=122)

    def __str__(self) -> str :
        return self.subjectName
    

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

class Subject_marks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} {self.subject.subjectName}"
    
    class Meta:
        unique_together = ['student','subject']

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    report_card_generated_date = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['student_rank','report_card_generated_date']
