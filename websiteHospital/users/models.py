from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    categories = (('Obstetricians and gynecologists', 'Obstetricians and gynecologists'), ('Psychiatrists', 'Psychiatrists'), ('Neurologists', 'Neurologists'), ('Cardiologists', 'Cardiologists'))
    #week = (('Friday', 'Friday'), ('Saturday', 'Saturday'),('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'))
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=100, choices=categories)
    details = models.TextField()
    visitingHour = models.CharField(max_length=15)
    visitingDates = models.CharField(max_length=30)
    dailyoccupation = models.IntegerField(default=0)


class Patient(models.Model):
    name = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    age = models.IntegerField(default=None, null=True)
    phone = models.CharField(max_length=15)
    doctors = models.ManyToManyField(Doctor)
    date = models.DateTimeField(default=timezone.now)
    appointment = models.DateField(null=True)
    serial = models.IntegerField(null=True)


    def age_cal(self):

        d = datetime.date.today() - self.dob
        d = int(d.days/365)
        self.age = d

    """
    def save(self, *args, **kwargs):
        self.is_adult()
        super(MyModel, self).save(*args, **kwargs)
    """



