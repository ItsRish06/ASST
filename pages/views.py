from django.shortcuts import render
from people.models import UnknownVisitor,Visitor,People,Role
from people.forms import *
from accounts.forms import *
from django.shortcuts import redirect
import datetime
from django.db.models import Avg
from itertools import chain
from operator import attrgetter

# Create your views here.

def loginPage(request):
    form = CustomUserCreationForm()


def visitors(request):
    visitors = Visitor.objects.all()
    unKnown = UnknownVisitor.objects.all()
    result_list = sorted(
    chain(visitors, unKnown),
    key=attrgetter('date_time'),
    reverse=True)
    context = {
        'visitors' : result_list
    }

    return render(request,'visitors.html',context)

def addVisitors(request):
    form = VisitorForm()
    form1 = UnknownVisitorForm()
    if request.method=="POST":
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
    


def dashboardView(request):
    visitors = Visitor.objects.all().filter(date_time__gte = datetime.date.today())
    visitorsNumber = visitors.count()
    temp = visitors.aggregate(Avg('temp'))
    tempNum = (temp['temp__avg'])
    if  tempNum == None:
        tempNum = 0
    try:
        highest = visitors.order_by('-temp')[0]
    except:
        highest = None
    if highest == None:
        highest = 0
    else:
        highest = highest.temp
    context ={
        'visitors':visitorsNumber,
        'temp':int(tempNum),
        'highest':int(highest)
    }

    return render(request,'dashboard.html',context)


def residentView(request):
    people = People.objects.all().filter(role__title__contains = 'Resident')

    context = {
        'people':people
    }

    return render(request,'residents.html',context)

def staffView(request):
    people = People.objects.all().filter(role__title__contains = 'Staff')

    context = {
        'people':people
    }

    return render(request,'staff.html',context)