from django.shortcuts import render, redirect
from . forms import StudentRegister
from .models import Student
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentRegister(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        stu = Student(name=name, email=email, password=password)
        stu.save()
        return redirect('student-list')
    else:
        form = StudentRegister()
    return render(request, 'enroll/home.html', {'form':form})


def studentList(request):
    form = Student.objects.all()
    return render(request, 'enroll/studentlist.html', {'form':form})

def deleteStudent(request, id):
    pop = Student.objects.get(id=id)
    pop.delete()
    return redirect('student-list')

def updateStudent(request, id):
    if request.method == 'POST':
        query = Student.objects.get(id=id)
        form = StudentRegister(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        query = Student.objects.get(id=id)
        form = StudentRegister(instance=query)
    return render(request, 'enroll/update.html', {'form':form})