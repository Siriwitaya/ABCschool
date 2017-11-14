from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):

    LEVEL_YEAR = (
        ('9', 'year 9'),
        ('10', 'year 10'),
        ('11', 'year 11'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    parent_name_eng = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=10)
    parent_email = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=1, choices=LEVEL_YEAR)
    grade = models.CharField(max_length=1, choices=LEVEL_YEAR)

    def publish(self):
        self.reg_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name_eng
        
class Teacher(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    tea_phone = models.CharField(max_length=10)
    tea_email = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)


    def publish(self):
        self.reg_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name_eng
        
