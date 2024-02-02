from django.db import models
from django.utils.html import escape


# Create your models here.

class user(models.Model):
    
     usertype=models.CharField(max_length=30,null=False,default="user")
     name=models.CharField(max_length=30,null=False)
     email=models.EmailField(max_length=20,primary_key=True)
     password=models.CharField(max_length=30,null=False)

     def __str__(self):
        return self.email

class hospital(models.Model):
    usertype=models.CharField(max_length=30,null=False,default="hospital")
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30,null=False)

    def __str__(self):
        return self.email

class ambulance(models.Model):
    usertype=models.CharField(max_length=30,null=False,default="ambulance")
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.email

class av_ambulance(models.Model):
    
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=30,null=False,primary_key=True)
    phNo=models.CharField(max_length=12,null=False)
    Street=models.CharField(max_length=50,null=False)
    City=models.CharField(max_length=50,null=False)
    State=models.CharField(max_length=50,null=False)
    Zip=models.CharField(max_length=30,null=False)
    NoOfAmb=models.CharField(max_length=3,null=False)
    Ambulance_email=models.ForeignKey(ambulance, on_delete=models.CASCADE,default="medisquarehospital@gmail.com")

    def __str__(self):
        return self.email
   
class av_hospital(models.Model):
    
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=30,null=False,primary_key=True)
    phNo=models.CharField(max_length=12,null=False)
    Street=models.CharField(max_length=50,null=False)
    City=models.CharField(max_length=50,null=False)
    State=models.CharField(max_length=50,null=False)
    Zip=models.CharField(max_length=30,null=False)
    Hospital_email=models.ForeignKey(hospital, on_delete=models.CASCADE,default="medisquarehospital@gmail.com")

    def __str__(self):
        return self.email

class patient(models.Model):

    fname=models.CharField(max_length=30,null=False)
    midname=models.CharField(max_length=30,default="")
    lname=models.CharField(max_length=30,null=False)
    dateOfRequest=models.CharField(max_length=8,null=False)
    timeOfRequest=models.CharField(max_length=8,null=False)
    am_pm=models.CharField(max_length=8,null=False)
    email=models.EmailField(max_length=20,primary_key=True)
    phNo=models.CharField(max_length=10,null=False)
    pickupStreet=models.CharField(max_length=50,null=False)
    pickupCity=models.CharField(max_length=50,null=False)
    pickupState=models.CharField(max_length=50,null=False)
    pickupZip=models.CharField(max_length=30,null=False)
    desstreet=models.CharField(max_length=50,null=False)
    descity=models.CharField(max_length=50,null=False)
    desstate=models.CharField(max_length=50,null=False)
    desZip=models.CharField(max_length=30,null=False)
    dob=models.CharField(max_length=30,null=False)
    gender=models.CharField(max_length=15,null=False)
    relation=models.CharField(max_length=30,null=False)
    medical_con=models.CharField(max_length=30,null=False)
    resonForAmb=models.CharField(max_length=30,null=False)
    User_gmail=models.ForeignKey(user, on_delete=models.CASCADE)
    # Amb_gmail=models.ForeignKey(ambulance, on_delete=models.CASCADE)
    # AvAmb_gmail=models.ForeignKey(av_ambulance, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname+' '+self.email


class hos_patient(models.Model):

    fname=models.CharField(max_length=30,null=False)
    midname=models.CharField(max_length=30,null=True,blank=True)
    lname=models.CharField(max_length=30,null=False)
    dateOfRequest=models.CharField(max_length=10,null=False)
    timeOfRequest=models.CharField(max_length=8,null=False)
    am_pm=models.CharField(max_length=8,null=False)
    email=models.EmailField(max_length=20,primary_key=True)
    phNo=models.IntegerField(max_length=10,null=False)
    Street=models.CharField(max_length=50,null=False)
    City=models.CharField(max_length=50,null=False)
    State=models.CharField(max_length=50,null=False)
    Zip=models.CharField(max_length=30,null=False)
    dob=models.CharField(max_length=30,null=False)
    gender=models.CharField(max_length=15,null=False)
    relation=models.CharField(max_length=30,null=False)
    medical_con=models.CharField(max_length=30,null=False)
    resonForHos=models.CharField(max_length=30,null=False)
    hospital=models.CharField(max_length=50,null=True)
    User_gmail=models.ForeignKey(user, on_delete=models.CASCADE)
    AvHospital_gmail=models.ForeignKey(av_hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname+' '+self.email

class Emergency(models.Model):
    current_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    city=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return f"Emergency {self.pk}"


    