from django.shortcuts import render
from people.models import UnknownVisitor,Visitor,People,Role
from people.forms import *
from accounts.forms import *
from django.shortcuts import redirect
import datetime
from django.db.models import Avg
from itertools import chain
from operator import attrgetter
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import statistics
from .utils import sendMail

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request,email = email,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Email OR Password is incorrect')
        context = {}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def visitors(request):

    search = request.GET.get('search')
    date = request.GET.get('date')
    print(type(date))
    visitors = Visitor.objects.all()
    unknown = UnknownVisitor.objects.all()

    if search:
        visitors = visitors.filter(name__name__icontains=search)
        unknown = unknown.filter(name__icontains=search)

    if date:
        visitors = visitors.filter(date_time__gte = date,date_time__lte = date+' 23:59')
        unknown = unknown.filter(date_time__gte = date,date_time__lte = date+' 23:59')
        print(visitors[0].date_time)

    result_list = sorted(
    chain(visitors, unknown),
    key=attrgetter('date_time'),
    reverse=True)

    context = {
        'visitors' : result_list
    }

    return render(request,'visitors.html',context)

@login_required(login_url='login')
def addVisitors(request):
    if not request.user.is_admin :
        return redirect('dashboard')
    form = VisitorForm()
    form1 = UnknownVisitorForm()
    if request.method=="POST":
        people = People.objects.get(id = request.POST.get('name'))
        info = {
            "name":people.name,
            "temp":int(request.POST.get('temp'))
        }
        if info['temp']>37:
            sendMail(info)
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form':form,
        'form1':form1
    }
    return render(request,'addVisitor.html',context)

def unknownForm(request):
    form = UnknownVisitorForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('addVisitor')
    

@login_required(login_url='login')
def dashboardView(request):
    visitors = Visitor.objects.all().filter(date_time__gte = datetime.date.today())
    unknown = UnknownVisitor.objects.all().filter(date_time__gte = datetime.date.today())
    visitorsNumber = visitors.count()
    unknownVisitorsNumber = unknown.count()
    totalCount = visitorsNumber+unknownVisitorsNumber
    l1=[]
    temp1 = visitors.aggregate(Avg('temp'))
    temp2 = unknown.aggregate(Avg('temp'))
    if  temp1['temp__avg'] != None :
        l1.append(temp1['temp__avg'])
    if  temp2['temp__avg'] != None :
        l1.append(temp2['temp__avg'])
    if len(l1) == 0:
        temp = 0
    else:    
        temp = statistics.mean(l1)
    
    try:
        highest1 = visitors.order_by('-temp')[0]
    except:
        highest1 = None
    if highest1 == None:
        highest1 = 0
    else:
        highest1 = highest1.temp

    try:
        highest2 = unknown.order_by('-temp')[0]
    except:
        highest2 = None
    if highest2 == None:
        highest2 = 0
    else:
        highest2 = highest2.temp

    if highest1>highest2:
        highest = highest1
    else:
        highest=highest2
    
    context ={
        'visitors':totalCount,
        'temp':int(temp),
        'highest':int(highest)
    }

    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def residentView(request):
    people = People.objects.all().filter(role__title__contains = 'Resident')

    context = {
        'people':people
    }

    return render(request,'residents.html',context)

@login_required(login_url='login')
def staffView(request):
    people = People.objects.all().filter(role__title__contains = 'Staff')

    context = {
        'people':people
    }

    return render(request,'staff.html',context)