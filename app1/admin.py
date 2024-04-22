from django.contrib import admin
from app1.models import *
from django.db.models import Sum
# Register your models here.
class admins(admin.ModelAdmin):
    cls=("recipe_name","recipe_desc","recipe_img","user")
admin.site.register(recipe,admins)


admin.site.register(studentid)
admin.site.register(department)
admin.site.register(student)
admin.site.register(subject)


class subjectmarkadmin(admin.ModelAdmin):
     dis=['student','subject','marks']
admin.site.register(studentmarks,subjectmarkadmin)

class reportcardadmin(admin.ModelAdmin):
    dis=['Student12','Student_rank_12','total_marks','date_o_report']

    def total_marks(self,obj):
        subject_marks=studentmarks.objects.filter(Student12=obj.student)
        marks=subject_marks.aggregate(marks=Sum('marks'))
        
        return marks
    
admin.site.register(reportcard,reportcardadmin)