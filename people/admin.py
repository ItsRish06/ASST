from django.contrib import admin
from .models import (People,Role,Visitor,UnknownVisitor)

# Register your models here.
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name','temp','date_time')
    search_fields=('name',)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name','role','contact','registration_date')
    search_fields=('name','role')


admin.site.register(People,PeopleAdmin)
admin.site.register(Role)
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(UnknownVisitor,VisitorAdmin)