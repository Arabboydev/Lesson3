from django.shortcuts import render
from .models import Products, Category

def get_info(request):
    catigories = Category.objects.all()
    context = {
        'catigories': catigories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Products.objects.filter(category=pk)
    context = {
        'products':products
    }
    return render(request, 'products.html', context=context)

def get_detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request,'detail.html',context=context)