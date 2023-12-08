from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import client,client_car
from datetime import datetime
import re
# from django.views.decorators.csrf import ensure_csrf_cookie

# from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return render(request,"index1.html")

def nissan(request):
    return render(request,"nissan1.html")

def client_details(request):
        return render(request,'client_details.html')

  
def new(request):
    if request.method == 'POST':
        
        # <--client dtails-->
        
        print(request.POST)
        Firstname = request.POST.get('firstname',None)
        # response_text = f'Param1: {Firstname}'
        return HttpResponse(Firstname)
    
    
    
def dataclient(request):
    if request.method == 'POST':
        
        # <--client dtails-->
        
        Firstname = request.POST.get('firstname',None)
        # response_text = f'Param1: {Firstname}'
        print(Firstname)
        return HttpResponse(Firstname)
        
        
# def dataclient(request):
#     if request.method == 'POST':
        # client dtails
        
        # Firstname = request.POST.get('firstname',None)
        # response_text = f'Param1: {Firstname}'
        # print(Firstname)
        # return HttpResponse(Firstname)
        # Lastname = request.POST.get('lastname')
        # Address = request.POST.get('Address')
        # phone_number = request.POST.get('Phone')
        # Dateofbirth = str(request.POST.get('Dob'))
        # try:
        #     Dob = datetime.strptime(Dateofbirth,'%Y-%m-%d')
        # except ValueError:
        #     print("Incorrect")
        #     return render(request,'client_details.html',{'message':"Invalid Date of Birth"})
        # cur_datetime = datetime.now()
        # date_time = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
        # # print(date_time)
        # District = request.POST.get('district')
        # State = request.POST.get('state')
        
        # phone number validation
        # matches = re.search("[8-9]\d{9}",phone_number)
        # print(matches)
        # if matches: Phone= matches; print(Phone)
        # elif matches == None : return render(request,'client_details.html',{'message':"Invalid Phone number"})
        # else: return render(request,'client_details.html')
        # elif matches == []: return render(request,'client_details.html',{'message':"3 number"})
        # else: return render(request,'client_details.html',{'message':"Invalid Phone number"})
        
        
        # # car details
        # modelname = request.POST.get('ModelName')
        # modelno = request.POST.get('ModelNo')
        # price = request.POST.get('Price')
        # fueltype = request.POST.get('FuelType')
        # transmission = request.POST.get('Transmission')
        # engineSize = request.POST.get('EngineSize')
        # mileage = request.POST.get('Mileage')
        # warranty = request.POST.get('Warranty')
        # seatingcapacity = request.POST.get('SeatingCapacity')
        # size = request.POST.get('Size')
        # fueltank = request.POST.get('FuelTank')
        # subject = request.POST.get('subject')
        
        
        # add new row client table and client table
        
        # user = client(current_datetime=date_time,firstname=Firstname,lastname=Lastname,
        #               address=Address,phone_number=phone_number,date_of_birth=Dob,district=District,state=State).save()
        # client_field = client.objects.all().last()
        # car_details = client_car(client_id = client_field.id,modelname=modelname,modelno=modelno,Price=price,fueltype=fueltype,transmission=transmission,
        #                               engine_size=engineSize,Mileage=mileage,Warranty=warranty,seating_capacity=seatingcapacity,
        #                               size=size,fueltank=fueltank,subject=subject).save()
        # car_field=client_car.objects.all().last()
        # return render(request,'client_details.html')
    
        # return HttpResponse("client_id :"+str(client_field.id)+" car_modelname: "+car_field.modelname+" car_id: "+str(car_field.id))
        # for k in all_field:
        #     return HttpResponse(k.id+" "+k.firstname)

        
def login(request):
    return render(request,"login_index.html")
        
        