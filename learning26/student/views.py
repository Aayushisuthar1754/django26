from django.shortcuts import render,redirect
from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def studentHome(request):
    return render(request,"studentHome.html")
def studentDashboard(request):
    student = {"name":"raj","age":23,"city":"Ahmedabad"}
    return render(request,"student/studentDashboard.html",student)    
    #student/studentDashboard.html
    #folder/filename

def servicelist(request):
    services = [
        {"name":"Web Development","price":500},
        {"name":"App Development","price":1000},
        {"name":"SEO Optimization","price":300},
    ]
    return render(request, "student/servicelist.html", {"services": services})

def createService(request):
     if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
        else:
            return render(request,"student/createservice.html",{"form":form})    
     else:
        form = StudentForm()
        return render(request,"student/createservice.html",{"form":form})

