from django.db import models
from django.contrib.auth.models import User



class Payment(models.Model):

    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    payment_ID = models.CharField(max_length=250)


    def __str__(self) -> str:
        return str(self.name)