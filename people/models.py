from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save

# Create your models here.

def upload_location(instance,filename):
    file_path = 'people/profilePic/{name}_{filename}'.format(
        name = str(instance.name),filename=filename
    )
    return file_path

class Role(models.Model):
    title = models.CharField(max_length= 150)

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(default='avatar.png',upload_to=upload_location,null=True,blank=True)
    contact = models.CharField(max_length=150)
    address = models.TextField(max_length=2000)
    role = models.ForeignKey(Role,on_delete = models.DO_NOTHING )
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Visitor(models.Model):
    name = models.ForeignKey(People,on_delete=models.DO_NOTHING)
    temp = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class UnknownVisitor(models.Model):
    name = models.CharField(max_length=150)
    temp = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=500,null=True,blank=True)
    visiting = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name


@receiver(post_delete,sender=People)
def submission_delete(sender,instance,*args,**kwargs):
    instance.image.delete(False)
