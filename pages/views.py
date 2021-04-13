from django.shortcuts import render
from people.models import *
from people.forms import *
from accounts.forms import *
from django.shortcuts import redirect

# Create your views here.

def loginPage(request):
    form = CustomUserCreationForm()


def visitors(request):
    visitors = Visitor.objects.all().order_by('-date')
    context = {
        'visitors' : visitors
    }

    return render(request,'visitors.html',context)

def addVisitors(request):
    form = VisitorForm()
    form1 = UnknownVisitor()
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
    form = UnknownVisitor(request.POST)
    print(form)
    print("hello")
    if form.is_valid():
            form.save()
            return redirect('addVisitor')
    
