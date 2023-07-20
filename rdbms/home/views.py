from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import city,area,road,accidents,complaint
from .forms import accidents_reportedForm, complaintForm
# Create your views here.
def home(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password,is_staff=True)
        if user is not None:
            login(request,user)
            return redirect('search')
        else:
            print('invalid')
    else:
        print('2 invaild')
    
    return render(request,"home.html")

def signup(request):
  
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        mail=request.POST['email']
        password=request.POST['password']
        con_password=request.POST['con_password']

        if password==con_password:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=mail).exists():
                print('email exist')
            else:
                user=User.objects.create_user(username=username,password=password,email=mail,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('home')

    
    return render(request,"signup.html")

def search(request):
    cityName=city.objects.all()
    return render(request,'search.html',{'cityName':cityName})




def areas(request,city_id):
    area_list=area.objects.filter(city_id=city_id).values()
    return render(request,'area.html',{'area_list':area_list})

def choice(request,area_id):
    # road_id=road.objects.filter(area_id=area_id).values()
    # acc_id=accidents.objects.filter(road_id=area_id).values()
    # try:  
    #     road_id=road.objects.get(area_id=area_id).pk
    #     acc_id=accidents.objects.get(road_id=area_id).pk
        
    # except:
    #     pass      
    return render(request,'choice.html',{'area_id':area_id})

def roads(request,area_id):

    # posts=road.objects.raw("select * from public.home_road where name='LBS Road'")
    roadNames=road.objects.filter(area_id=area_id).values()
    return render(request,'roads.html',{'roadName':roadNames,})
    
def accidentss(request,area_id):
    acc=accidents.objects.filter(road_id=area_id).values()
    return render(request,'accidentss.html',{'acc':acc})

def complaints(request):
    if request.method=="POST":
        form = complaintForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('complaint_registered')
    form=complaintForm
    return render(request,'complaint.html',{'form':form})

def report(request):
    return render(request,'report.html',{})

def complaint_registered(request):
    return render(request,'complaint_registered.html')

def report(request):
    if request.method=="POST":
        form = accidents_reportedForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accidents_registered')   
    form=accidents_reportedForm
    return render(request,'report.html',{'form':form})

def accidents_registered(request):
    return render(request,'accidents_registered.html')