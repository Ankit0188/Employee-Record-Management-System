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
    empjoinningdate = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100, null=True)
    schoolcollegepg = models.CharField(max_length=200, null=True)
    yearofpassingpg = models.CharField(max_length=20, null=True)
    cgpapg = models.CharField(max_length=30, null=True)

    courseg = models.CharField(max_length=100, null=True)
    schoolcollegeg = models.CharField(max_length=200, null=True)
    yearofpassingg = models.CharField(max_length=20, null=True)
    cgpag = models.CharField(max_length=30, null=True)

    coursehsc = models.CharField(max_length=100, null=True)
    schoolcollegehsc = models.CharField(max_length=200, null=True)
    yearofpassinghsc = models.CharField(max_length=20, null=True)
    cgpahsc = models.CharField(max_length=30, null=True)

    coursessc = models.CharField(max_length=100, null=True)
    schoolcollegessc = models.CharField(max_length=200, null=True)
    yearofpassingssc = models.CharField(max_length=20, null=True)
    cgpassc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100, null=True)
    company1designation = models.CharField(max_length=100, null=True)
    company1salary = models.CharField(max_length=100, null=True)
    company1duration = models.CharField(max_length=100, null=True)
    company2name = models.CharField(max_length=100, null=True)
    company2designation = models.CharField(max_length=100, null=True)
    company2salary = models.CharField(max_length=100, null=True)
    company2duration = models.CharField(max_length=100, null=True)
    company3name = models.CharField(max_length=100, null=True)
    company3designation = models.CharField(max_length=100, null=True)
    company3salary = models.CharField(max_length=100, null=True)
    company3duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
