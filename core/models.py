from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100)
    somebodys_adress = models.ForeignKey(
        'Adress', on_delete=models.SET_NULL, blank=True, null=True)
    #pod jednym adresem moze zyc wiele osob
    somebodys_phone = models.ForeignKey(
        'Phone', on_delete=models.SET_NULL, blank=True, null=True
    )
    somebodys_emails = models.ForeignKey(
        'Email', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Adress(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.IntegerField
    flat_number = models.IntegerField

class Phone(models.Model):
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=20)

class Email(models.Model):
    email = models.CharField(max_length=50)
    email_type = models.CharField(max_length=20)

class Gropus(models.Model):
    name = models.CharField(max_length=30)
    group = models.ManyToManyField(Person)

