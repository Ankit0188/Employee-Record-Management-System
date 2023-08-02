from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        empco = request.POST['empcontact']
        ei = request.POST['emailid']
        ad = request.POST['address']
        pw = request.POST['apv']
    try:
        user = User.objects.create_user(first_name=fn, last_name=ln, username=ei, password=pw)
        EmployeeDetail.objects.create(user=user, empcontact=empco)
        EmployeeExperience.objects.create(user=user)
        EmployeeEducation.objects.create(user=user)
        error = "no"
        return render(request, 'emp_login.html')
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
    return redirect('emp_login')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        department = request.POST['empdept']
        designation = request.POST['empdesignation']
        ei = request.POST['emailid']
        contact = request.POST['empcontact']
        ad = request.POST['address']
        code = request.POST['empcode']
        joinning = request.POST['empjoinningdate']
        gender = request.POST['empgender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empdept = department
        employee.empdesignation = designation
        employee.user.empcontact = contact
        employee.user.email = ei
        employee.user.address = ad
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


def admin_login(request):
    return render(request, 'admin_login.html')


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request, 'my_experience.html', locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation = request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1designation = company1designation
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2designation = company2designation
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3designation = company3designation
        experience.company3salary = company3salary
        experience.company3duration = company3duration

    try:
        experience.save()

        error = "no"
    except:
        error = "yes"
    return render(request, 'edit_experience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request, 'my_education.html', locals())


def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolcollegepg = request.POST['schoolcollegepg']
        yearofpassingpg = request.POST['yearofpassingpg']
        cgpapg = request.POST['cgpapg']

        courseg = request.POST['courseg']
        schoolcollegeg = request.POST['schoolcollegeg']
        yearofpassingg = request.POST['yearofpassingg']
        cgpag = request.POST['cgpag']

        coursehsc = request.POST['coursehsc']
        schoolcollegehsc = request.POST['schoolcollegehsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        cgpahsc = request.POST['cgpahsc']

        coursessc = request.POST['coursessc']
        schoolcollegessc = request.POST['schoolcollegessc']
        yearofpassingssc = request.POST['yearofpassingssc']
        cgpassc = request.POST['cgpassc']

        education.coursepg = coursepg
        education.schoolcollegepg = schoolcollegepg
        education.yearofpassingpg = yearofpassingpg
        education.cgpapg = cgpapg

        education.courseg = courseg
        education.schoolcollegeg = schoolcollegeg
        education.yearofpassingg = yearofpassingg
        education.cgpag = cgpag

        education.coursehsc = coursehsc
        education.schoolcollegehsc = schoolcollegehsc
        education.yearofpassinghsc = yearofpassinghsc
        education.cgpahsc = cgpahsc

        education.coursessc = coursessc
        education.schoolcollegessc = schoolcollegessc
        education.yearofpassingssc = yearofpassingssc
        education.cgpassc = cgpassc

    try:
        education.save()

        error = "no"
    except:
        error = "yes"
    return render(request, 'edit_education.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_password.html', locals())


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['apv']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'admin_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def admin_Logout(request):
    logout(request)
    return redirect('admin_login')


def change_adminpassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_adminpassword.html', locals())


def all_employees(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employees = EmployeeDetail.objects.all()
    return render(request, 'all_employees.html', locals())


def delete_profile(request, pid):
    try:
        employee = EmployeeDetail.objects.get(pk=pid)
        employee.user.delete()  # Deletes the associated User model
        employee.delete()  # Deletes the EmployeeDetail model
        return redirect('all_employees')  # Redirect to a page displaying the list of employees
    except EmployeeDetail.DoesNotExist:
        # If the employee with the given emp_id doesn't exist, handle the exception as needed
        return redirect('all_employees')  # Redirect to a page displaying the list of employees with a message
