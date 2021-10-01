from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Proffesional_detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    gender = models.CharField(max_length=150)
    phone_Number = models.CharField(max_length=150)
    adhaar_Number = models.CharField(max_length=150)
    native_Place = models.CharField(max_length=150)
    date_Of_Birth = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)
    departments = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    occupation_Location=models.CharField(max_length=150,null=True)
    office_Levels = models.CharField(max_length=150,null=True)
    office_Location = models.CharField(max_length=150,null=True)
    organisation = models.CharField(max_length=150,null=True)
    districts = models.CharField(max_length=150, null=True)
    constituency = models.CharField(max_length=150, null=True)
    mandal = models.CharField(max_length=150, null=True)
    panchayath = models.CharField(max_length=150, null=True)
    village = models.CharField(max_length=150, null=True)
    central_Organisation = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return str(self.user.username)







