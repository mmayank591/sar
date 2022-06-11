from contextvars import Context
import email
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import  datetime

from numpy import save
from home.models import Contact
from django.contrib import messages
def index (request):
    context= {'variable':"this is sent"}
    return render(request,'index.html',context)
     
   
   
   
    # return HttpResponse("this is home page")
# Create your views here.
def contact (request):
    if request.method == "POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            desc=request.POST.get('desc')
            contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
            contact.save()
            messages.success(request, 'Your opinion means the world to us will contact you soon!!')
            
    return render(request,'contact.html')
     
   
    #return HttpResponse("HELLO THERE!!,    WE BUILD WEBSITES FOR YOUR START UP'S !!  CONTACK US AT -881781837   (MAYANK MISHRA)  ")
def mail (request):
    return render(request,'mail.html')

def link(request):
    return render(request,'link.html')
def home1(request):
    return render(request,'index.html')

   #  return HttpResponse("MAIL US AT-  mmayank591@gmail.com")    