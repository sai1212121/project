from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipe(models.Model): 
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name=models.CharField(max_length=200)
    recipe_desc=models.TextField()
    recipe_img=models.ImageField(upload_to="recipe")
class department(models.Model):
    studentbranch=models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.studentbranch
    class Meta:
        ordering=['studentbranch']

class studentid(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id    


class subject(models.Model):
    sub_name=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.sub_name

class student(models.Model):
    student_name=models.CharField(max_length=150)
    student_age=models.IntegerField()
    student_branch=models.ForeignKey(department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(studentid,related_name="studentid",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student_name
    class Meta:
        ordering=['student_name']
        verbose_name='student'

class studentmarks(models.Model):
    student=models.ForeignKey(student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    marks=models.IntegerField()


    def __str__(self) -> str:
        return f'{self.student.student_name}{self.subject.sub_name}'
    
    class Meta:
        unique_together=['student','subject']
    


class reportcard(models.Model):
    Student12=models.ForeignKey(student,related_name="studentreportcard",on_delete=models.CASCADE)
    Student_rank_12=models.IntegerField()
    date_o_report=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=['Student_rank_12','date_o_report']