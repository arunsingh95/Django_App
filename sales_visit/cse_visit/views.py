import requests

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


from .models import *
from .forms import CustomerEditForm

# url = 'http://127.0.0.1:8000'
url = 'http://192.168.42.93:8000'


def register(request):
    if request.method == 'GET':
        return render(request, 'cse_visit/register.html')
    elif request.method == 'POST':
        error_message = ''
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('InputPassword')
        confirm_password = request.POST.get('confirmInputPassword')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if password == confirm_password:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('/')
        else:
            error_message = "password and current password do not match"
        context = {
            'message': error_message
        }
        return render(request, 'cse_visit/register.html', context)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'cse_visit/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('InputPassword')
        user = authenticate(request, username=username, password=password)
        user_logged_in = User.objects.get(id=user.id)
        if user is not None:
            login(request, user)
            print(user.username, user.id)
            print('1111', user_logged_in.active.is_logged_in)
            user_logged_in.active.is_logged_in = True
            print('2222', user_logged_in.active.is_logged_in)
            user_logged_in.active.name = 'logged in hogaya hai'
            user_logged_in.save()
            return redirect('dashboard')
        else:
            error_message = "username or password is invalid"
            return render(request, 'cse_visit/login.html', {'message': error_message})


def user_logout(request):
    user = User.objects.get(id=request.user.id)
    user.active.is_logged_in = False
    user.active.name = 'log out hogaya'
    user.save()
    logout(request)
    return redirect('/')


def dashboard(request):
    params = {}
    if not request.user.is_superuser:
        params = {'assigned_cse': request.user.id}
    response_data = requests.get(url=f"{url}/api/customer_details", params=params)
    context = {
        'data': response_data.json(),
        'assign_cse': User.objects.all(),
        'branch': Branch.objects.all(),
        'status': Status.objects.all(),
        'logged_in':  User.objects.filter(active__is_logged_in=True)
    }
    return render(request, 'cse_visit/dashboard.html', context)


def add_customer(request):
    data = {}
    # add_customer_url = "http://127.0.0.1:8000/api/customer_details/"
    add_customer_url = "http://http://192.168.42.93:8000/api/customer_details/"
    data['customer_name'] = request.POST.get('exampleInputName')
    data['branch'] = request.POST.get('exampleInputBranch')
    data['assigned_cse'] = request.POST.get('exampleInputCSE')
    data['visit_date'] = request.POST.get('exampleInputVisit_date')
    data['customer_address'] = request.POST.get('exampleInputAddress')
    data['status'] = 1
    response = requests.post(url=add_customer_url, json=data)
    return redirect('dashboard')


def edit_customer(request, id):
    data = {}
    # url = f"http://127.0.0.1:8000/api/customer_details/edit/{id}"
    url = f"http://http://192.168.42.93:8000/api/customer_details/edit/{id}"
    response = requests.get(url=url)
    form = CustomerEditForm()
    context = {
        'data': response.json(),
        'assign_cse01': User.objects.all(),
        'branch01': Branch.objects.all(),
        'form': form
        }
    if request.method == 'POST':
        model = CustomerVisitDetails.objects.get(id=id)
        X = request.FILES
        model.attachment = X.get('attachment')
        model.is_submitted = True
        model.save()
        return redirect('dashboard')
    return render(request, 'cse_visit/edit_customer.html', context)


def edit_status(request):
    customer = request.GET.get('customer')
    status = request.GET.get('status')
    X = CustomerVisitDetails.objects.filter(id=customer).update(**{'status': status})
    return HttpResponse('done')


def reports(request):
    params = {}
    if not request.user.is_superuser:
        params = {'assigned_cse': request.user.id}
    report_data = requests.get(url=f"{url}/api/customer_details", params=params)
    return render(request, 'cse_visit/reports.html', {'report_data': report_data.json()})


# def logged_in_users(request):
#     logged_user = User.objects.filter()