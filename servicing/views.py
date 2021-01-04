from django.shortcuts import render,redirect
from .models import Car,Service
from django.http import Http404
from django.shortcuts import get_object_or_404
from .forms import CarForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url="/login/")
def home(request):
   
    return render(request,'index.html')

@login_required(login_url="/login/")   
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
@login_required(login_url="/login/")
def cardetails(request,id):
    data = get_object_or_404(Car,pk = id)
    
    context = {'data':data}
    return render(request,'details.html',context)

@login_required(login_url="/login/")
def create_car(request):
    form  = CarForm(request.POST,request.FILES)
    if form.is_valid():
        newproject =form.save(commit=False)
        newproject.Images = request.FILES['Images']
        newproject.save()
        messages.info(request,'Succefully Saved')
        form = CarForm()
        return redirect('create')

    context = {
        'form':form
    }
   


    return render(request,'create.html',context)

@login_required(login_url="/login/")
def delete(request,id):
    car = Car.objects.get(id = id)
    if request.method =='POST':
        car.delete()
        return redirect('main')
    context = {
        'item':car
    }
    return render(request,'delete.html',context)




def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Exists !!')
                return redirect(signup)
            elif User.objects.filter(email = email).exists():
                messages.info(request,'enail already Exists !!')
            else:
                user = User.objects.create_user(username = username,password = password1,first_name = first_name,last_name = last_name)
                user.save()
                messages.info(request,'Created Succefully')
        else:
            messages.info(request,'Password not match')
            return redirect('signup')




    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password =password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credintial')
        return redirect('login')
    

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')




    

        
        

