from django.shortcuts import render
from people.models import *
from people.forms import *
from accounts.forms import *

# Create your views here.

def loginPage(request):
    form = CustomUserCreationForm()


def home(request):
    context = {"msg":"hello world!"}

    return render(request,'index.html',context)

