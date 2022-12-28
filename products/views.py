from django.http import HttpResponse

from django.shortcuts import render

from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    names = ['mani','dhana','aryan']
    return render(request, 'index.html', {'names':names})


def new(request):
    return HttpResponse('New products')

