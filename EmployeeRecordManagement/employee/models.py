from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EmployeeDetail(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=100, null=True)
    empdept = models.CharField(max_length=100, null=True)
    empdesignation = models.CharField(max_length=100, null=True)
    empcontact = models.CharField(max_length=15, null=True)
    empgender = models.CharField(max_length=50, null=True)
    empjoiningdate = models.DateField(null=True)
    empaddress = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
