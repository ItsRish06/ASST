from django.urls import path,include
from .views import visitors,addVisitors,unknownForm,dashboardView,residentView,staffView,loginPage,logoutUser
from django.views.generic import TemplateView

urlpatterns = [
    path('', dashboardView,name = "dashboard"),
    path('visitors', visitors,name = "visitors"),
    path('addVisitor',addVisitors,name = "addVisitor"),
    path('unknown',unknownForm,name = "unknown"),
    path('residents',residentView,name = "residents"),
    path('staff',staffView,name = "staff"),
    path('login',loginPage,name="login"),
    path('logout',logoutUser,name="logout")
]