from django.db import models

# Create your models here.
class Contact_US(models.Model):
    User_Name = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Subject = models.CharField(max_length=250)
    Message = models.CharField(max_length=250)

    def __str__(self):
        return str(self.User_Name)
