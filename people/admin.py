from django.contrib import admin
from .models import (Resident,Staff,Role,Visitor)

# Register your models here.
admin.site.register(Resident)
admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(Visitor)