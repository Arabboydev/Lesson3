from django.shortcuts import render
from .models import Student, Category

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_student(request, pk):
    students = Student.objects.filter(category=pk)
    context = {
        'students': students
    }
    return render(request, 'student.html', context=context)

def get_about(request, pk):
    student = Student.objects.get(pk=pk)
    context = {
        'student': student
    }
    return render(request, 'about.html', context=context)
