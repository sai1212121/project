from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Count, Min, Sum,Max
from .fake import send_mail_c
import re



# Create your views here.

def recipes(request):
    if request.method == "POST":

        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')
        recipe_img=request.FILES.get('recipe_img')
        

        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_img=recipe_img,

        
        )
        return redirect('/recipe')
    query_set=recipe.objects.all()
    context={'recippes': query_set}
    

    return render (request, "recipes.html",context)

def home(request):
    
    return render(request,"home.html")

def send_mail_client(request):
    send_mail_c()
    return redirect("/")


def deleteset(request,id):
    querset=recipe.objects.get(id=id)
    querset.delete()
    
    return redirect(request,'/recipe/')


def login_page(request):
    if request.method == "POST":
        username = request.POST["user__name"]
        password = request.POST["_password"]

        if not User.objects.filter(username = username).exists():
            messages.error(request,'invalid username')
            return redirect('/loginpage')

        user=authenticate(username= username,password= password)


        if user is not None:
            login(request,user)
            messages.info(request,'login sucessfully')
            return redirect('/recipe')
        
        else:
            
            return redirect('/loginpage')


    return render(request,"loginpage.html")


def register_page(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request,"user already exists")
            return redirect('/registerpage/')


       
        user = User.objects.create(
            first_name = first_name ,
            last_name = last_name ,
            username = username,
        )
    
        user.set_password(password)
        user.save()

        messages.info(request,'account created successfully')
        

        return redirect('/registerpage/')

       

        

    return render(request,"registerpage.html")




#def student_page(request):
 #   if request.method == "POST":
  #      name=request.POST.get("name")
   #     age=request.POST.get("age")
    #    branch=request.POST.get("branch")

    

   # return render(request,"studentinfo.html")
from django.db.models import Q

def get_studets(request):
    queryset=student.objects.all()
    rank=student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
    for i in rank:
       pass

    if request.GET.get('search'):
        search=request.GET.get('search')
       
        queryset=student.objects.filter(
            Q(student_name__icontains = search))
          
        
    
    paginator = Paginator(queryset, 50)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    

    return render(request,"studentinfo.html",{'queryset':page_obj})


def totalmarks(request,student_id):
   
    query=studentmarks.objects.filter(student__student_id__student_id= student_id)
    total_marks=query.aggregate(total_marks=Sum('marks'))
    
    
    current_rank=1
    rank=student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
    current_rank=current_rank
    for i in rank:
        if student_id == i.student_id.student_id:
            current_rank = current_rank
            
            
            break
        current_rank=current_rank+1
   
    return render(request,"totalmarks.html",{'query':query,'total_marks':total_marks,'current_rank':current_rank})

from .views import totalmarks

def analysis(request):
   
    rank=student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
    top_10_rankers=rank[0:11]
    top_10=[]
    for val in top_10_rankers:
       top_10.append(val)
        
    
    last_student=rank.order_by('marks')[1:3]
    avgrage_marks=rank.aggregate(Avg('marks'))
    count_of_students=rank.aggregate(Count('marks'))
    max_marks=rank.aggregate(Max('marks'))
    min_marks=rank.aggregate(Min('marks'))
    name_startswith=student.objects.filter(student_name__startswith='s')
    name_startswith_a=student.objects.filter(student_name__startswith='a')[1:5]
   
    
    data={
        'top':top_10,
        'last':last_student,
        'avg':avgrage_marks,
        'count':count_of_students,
        'marks':max_marks,
        'minmarks':min_marks,
        'namestartswith':name_startswith,
        'namestartwitha':name_startswith_a

    }
    

    
    return render(request,"operations.html",data)