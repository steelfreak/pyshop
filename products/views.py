from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index1(request):
    return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New Products')


def index(request):
    products=Product.objects.all()
    return render(request, 'index.html', {'products':products})
    

