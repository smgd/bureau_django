from django.db import models

from datetime import datetime

class Car(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    creation_date = models.DateField()
    disposal_date = models.DateField()
    passport = models.ImageField(upload_to='passports')

    def __str__(self):
        return self.vin