from django.shortcuts import render


# Create your views here.

def home(request):
    context = {}
    return render(request, 'responsive/home.html', context)

def products(request):
    context = {}
    return render(request, 'responsive/products.html', context)    

def people(request):
    context = {}
    return render(request, 'responsive/people.html', context)  

def contactus(request):
    context = {}
    return render(request, 'responsive/contactus.html', context)  


