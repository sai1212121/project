from faker import Faker
fake=Faker()
import random
from app1.models import *
import numpy as np
from django.db.models import Sum
from django.core.mail import send_mail
from appstall import settings

def create_subject_marks(n):
    try:

        student_obj=student.objects.all()
        for student1 in student_obj:
            subjects=subject.objects.all()
            for sub in subjects:
                studentmarks.objects.create(
                    student=student1,
                    subject=sub,
                    marks=random.randint(20,100)
                )
    except Exception as xp:
        print(xp)       

def save(n=10)->None:

   
    for i in range(0,n):
    # [1,2,3,4,5]
        deap_obj=department.objects.all()
        random_index=np.random.randint(0,len(deap_obj)-1)
        student_branch=deap_obj[random_index]
        student_name=fake.name()
        student_age=np.random.randint(20,50)
        student_id=f'std-0{np.random.randint(100,999)}'

        student_id_obj=studentid.objects.create(student_id=student_id)

        student_obj=student.objects.create(
            student_id=student_id_obj,
            student_branch=student_branch,
            student_name=student_name,
            student_age=student_age
        )
      
    

def generate_report_card():
    current_rank=1
    rank=studentmarks.objects.annotate(marks=Sum('studentmarks__marks')).order_by('marks')
    
    current_rank=current_rank
    for i in rank:
        print(i)
        reportcard.objects.create(
            Student12=i,
            Student_rank_12=current_rank
        )
        current_rank=current_rank+1


def send_mail_c(request):
    send_mail(
        "test mail",
        "hi this msg from django",
        settings.EMAIL_HOST_USER,
        ["saianumala5@gmail.com"]

    )
    