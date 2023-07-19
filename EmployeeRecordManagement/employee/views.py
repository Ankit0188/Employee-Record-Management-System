from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        empco = request.POST['empcontact']
        '''empc = request.POST['empcode']'''
        ei = request.POST['emailid']
        ad = request.POST['address']
        pw = request.POST['apv']
    try:
        user = User.objects.create_user(first_name=fn, last_name=ln, username=ei, password=pw)
        EmployeeDetail.objects.create(user=user, empcontact=empco, )
        error = "no"
    except:
        error = "yes"
    return render(request, 'registration.html', locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['apv']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    print('profile function is called')
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        print(request.POST)
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        department = request.POST['empdept']
        designation = request.POST['empdesignation']
        ei = request.POST['emailid']
        contact = request.POST['empcontact']
        ad = request.POST['empaddress']
        code = request.POST['empcode']
        joinning = request.POST['empjoinningdate']
        gender = request.POST['empgender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empdept = department
        employee.empdesigantion = designation
        employee.empcontact = contact
        employee.emailid = ei
        employee.address = ad
        employee.empcode = code
        employee.empgender = gender

        if joinning:
            employee.empjoinningdate = joinning

    try:
        employee.save()
        employee.user.save()
        error = "no"
    except:
        error = "yes"
    return render(request, 'profile.html', locals())
