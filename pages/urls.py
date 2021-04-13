from django.urls import path,include
from .views import visitors,addVisitors,unknownForm
from django.views.generic import TemplateView

urlpatterns = [
    path('', visitors,name = "visitors"),
    path('addVisitor',addVisitors,name = "addVisitor"),
    path('unknown',unknownForm,name = "unknown")

]