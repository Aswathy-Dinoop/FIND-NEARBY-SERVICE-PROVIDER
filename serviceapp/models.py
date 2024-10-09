from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)

class Add_Services(models.Model):
    service_name = models.CharField(max_length=50)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=6, decimal_places=2)

class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class ServicerRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    image=models.ImageField(null=True)
    regnum=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class Services(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    servicer=models.ForeignKey(ServicerRegistration,on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(Add_Services,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    price=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)
    image=models.ImageField(null=True)
    name=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)

class Requests(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    services=models.ForeignKey(Services,on_delete=models.CASCADE,null=True)
    provider=models.ForeignKey(ServicerRegistration,on_delete=models.CASCADE,null=True)
    bookingdate=models.CharField(max_length=22, null=True)
    bookingtime=models.CharField(max_length=22, null=True)
    status=models.CharField(max_length=22,null=True)
class Assign(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    services=models.ForeignKey(Services,on_delete=models.CASCADE,null=True)
    request=models.ForeignKey(Requests,on_delete=models.CASCADE,null=True)
    provider=models.ForeignKey(ServicerRegistration,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=22, null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    workstatus=models.CharField(max_length=25,null=True)
    paymentstatus=models.CharField(max_length=25,null=True)
    amount=models.CharField(max_length=25,null=True)



class Rating(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    workers=models.ForeignKey(Services,on_delete=models.CASCADE,null=True)
    star=models.CharField(max_length=22, null=True)
    comment=models.CharField(max_length=22, null=True)
    status = models.CharField(max_length=22, null=True)
    provider=models.ForeignKey(ServicerRegistration,on_delete=models.CASCADE,null=True)
