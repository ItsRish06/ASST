from django.db import models

# Create your models here.
class Resident(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    address = models.TextField(max_length=2000)
    management = models.BooleanField()
    society_head = models.BooleanField()

    def __str__(self):
        return self.name
    
class Role(models.Model):
    title = models.CharField(max_length= 150)

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=150)
    role = models.ForeignKey(Role,on_delete = models.DO_NOTHING )
    contact = models.CharField(max_length=150)
    address = models.TextField(max_length=2000)

    def __str__(self):
        return self.name



class Visitor(models.Model):
    name = models.CharField(max_length = 150)
    temp = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
