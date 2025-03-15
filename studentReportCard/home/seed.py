from faker import Faker
import random
from home.models import *
from django.db.models import Sum

fake = Faker()


def generate_student_rank():
    try:
        
        ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','student_age')    
        i=1
        

        for rank in ranks:
            print(rank)
            ReportCard.objects.create(
                student = rank,  # This is student object only.
                student_rank = i
            )
            i = i+1



    except Exception as e:
        print(e)

def create_subject_market():
    try:
        
        student_obj = Student.objects.all()

        # Loop for each student
        for student in student_obj:
            
            # Loop for each subhect and adding marks of each subject for that particular student
            subjects = Subject.objects.all()
            for subject in subjects:
                Subject_marks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                ) 

    except Exception as e:
        print(e)


def seed_db(n=10):
    try:
        for _ in range(0,n):        

            departments_obj = Department.objects.all()
            random_index = random.randint(0,len(departments_obj)-1)

            department = departments_obj[random_index]
            student_id =  f"STUD-0{random.randint(1,1000)}"

            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,25)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(studentId = student_id)
            
            Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)