from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allProds = [[products, range(1,nSlides),nSlides],
               [products, range(1,nSlides),nSlides]]
    params = {'allProds' : allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/prodview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')