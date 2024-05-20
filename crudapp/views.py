from django.shortcuts import render
from .models import*
# Create your views here.
def insertpage(request):
    if (request.method =="POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        data = Students.objects.create(firstname=fname,
                                      lastname=lname,
                                      email=email,
                                      address=address,
                                      phone=phone)
    return render(request,'insertpage.html')
def displaypage(request):
    data = Students.objects.all()
    return render(request,'displaypage.html',{'data':data})

def deletepage(request):
    data = Students.objects.all()
    return render (request,'deletepage.html',{'data':data})

def deletestudent(request,id):
    #id = request.POST.get("id")
    print("id :",id)
    obj=Students.objects.filter(id=id)
    Students.objects.filter(id=id).delete()
    data = Students.objects.all()
    return render (request,'deletepage.html',{'data':data})

def updatepage(request,):
    data = Students.objects.all()
    return render (request,'updatepage.html',{'data':data})

def editpage(request,id):
    obj = Students.objects.filter(id=id)
    data = obj[0]
    return render (request,'editpage.html',{'data':data})

def editstudent(request):
    if(request.method == "POST"):
        id = request.POST.get('id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        data= Students.objects.filter(id=id)[0]
        data.firstname = fname
        data.lastname = lname
        data.email = email
        data.address = address
        data.phone = phone
        data.save()
    return render (request,'editpage.html')
