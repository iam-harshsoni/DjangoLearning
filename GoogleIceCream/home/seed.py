from faker import Faker
import random
from home.models import *

fake = Faker()

def seed_db(n=100):
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