from django.shortcuts import render
from .models import Technology, Category

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'index.html', context=context)

def get_technology(request, pk):
    technologies = Technology.objects.filter(category_id=pk)
    context = {
        'technologies': technologies
    }
    return render(request, 'technology.html', context=context)

def detail(request, pk):
    technology = Technology.objects.get(pk=pk)
    context = {
        'technology': technology
    }
    return render(request, 'detail.html', context=context)