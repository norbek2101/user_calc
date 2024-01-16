from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Family(models.Model):
    name = models.CharField(max_length=50)

class Education(models.Model):
    level = models.CharField(max_length=50)

class BankingService(models.Model):
    name = models.CharField(max_length=50)

class Job(models.Model):
    title = models.CharField(max_length=50)

class PersonalTransport(models.Model):
    type = models.CharField(max_length=50)

class AlcoholConsumption(models.Model):
    level = models.CharField(max_length=50)

class Smoking(models.Model):
    status = models.CharField(max_length=50)

class Usrs(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    # categories = models.ManyToManyField(Category)
    # income = models.ForeignKey(Income, on_delete=models.SET_NULL, null=True, blank=True)
    # family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True)
    # education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, blank=True)
    # banking_service = models.ForeignKey(BankingService, on_delete=models.SET_NULL, null=True, blank=True)
    # job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    # personal_transport = models.ForeignKey(PersonalTransport, on_delete=models.SET_NULL, null=True, blank=True)
    # alcohol_consumption = models.ForeignKey(AlcoholConsumption, on_delete=models.SET_NULL, null=True, blank=True)
    # smoking = models.ForeignKey(Smoking, on_delete=models.SET_NULL, null=True, blank=True)



class Usrs(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)


#Place
class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Region(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)

class Place(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    users = models.ManyToManyField(Usrs)


#Gender and Age
#Categories 
#Income
#Family and Childer
# Education
# Banking services
# Job
#Personal Transport
# Alchohol consumption
# Smoking