from django.shortcuts import render,redirect
from .models import Car,Service
from django.http import Http404
from django.shortcuts import get_object_or_404



# Create your views here.

def home(request):
   
    return render(request,'index.html')

def main(request):
    cars = Car.objects.all()
    allProds = []
    catprods = Car.objects.values('category', 'id')
    
    #cat[prods] me se category nikalna
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Car.objects.filter(category=cat)
        allProds.append(prod)
        context = {'allProds': allProds}
    return render(request,'home.html',context)

def cardetails(request,id):
    data = get_object_or_404(Car,pk = id)
    
    context = {'data':data}
    return render(request,'details.html',context)




    

        
        

