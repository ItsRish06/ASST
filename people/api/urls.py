from django.urls import path,include
from .views import add_visitor

urlpatterns = [
    path('',add_visitor),


]