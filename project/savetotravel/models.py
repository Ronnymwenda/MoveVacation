from django.db import models
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    id_no=models.IntegerField(null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    role=models.CharField(max_length=20,null=True,blank=True)


class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    Hotel_name=models.CharField(max_length=50)
    Contact=models.BigIntegerField(null=True,blank=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    images=models.ImageField(upload_to='images/')
    Description=models.TextField(null=True,blank=True)

class Events(models.Model):
    id=models.IntegerField(primary_key=True)
    event_name=models.CharField(max_length=50,null=True,blank=True)
    event_date=models.DateField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True,blank=True)


class Payments(models.Model):
    id = models.IntegerField(primary_key=True)
    Amount=models.IntegerField(null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

class Booked_events(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    event=models.ForeignKey(Events, on_delete=models.CASCADE,null=True,blank=True)
    Payment=models.ForeignKey(Payments,on_delete=models.CASCADE,null=True,blank=True)

class Deposit(models.Model):
    id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    event=models.ForeignKey(Events, on_delete=models.CASCADE,null=True,blank=True)
    deposit=models.ForeignKey(Payments,on_delete=models.CASCADE,null=True,blank=True)
