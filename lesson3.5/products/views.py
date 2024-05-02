from django.shortcuts import render
from .models import Category,Waters

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,'index.html', context=context)

def get_waters(request, pk):
    waters = Waters.objects.filter(category=pk)
    context = {
        'waters': waters
    }
    return render(request,'waters.html', context=context)

def get_about(request, pk):
    water = Waters.objects.get(pk=pk)
    context = {
        'water': water
    }
    return render(request,'about.html', context=context)
