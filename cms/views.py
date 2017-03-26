from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from .forms import MyUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
@login_required
def main_list(request):
    companies = Company.objects.all().order_by('name')
    users = User.objects.all().order_by('username')
    return render(request, 'cms/main_list.html', {'companies': companies, 'users': users})


# Adding new companies
@login_required
def add_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.creator = request.user
            company.save()
            return redirect('main_list')
    else:
        form = CompanyForm()
    return render(request, 'cms/company_add.html', {'form': form})


# Adding new users
@login_required
def add_user(request):
    if request.method == "POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('main_list')
    else:
        form = MyUserForm()
    return render(request, 'cms/user_add.html', {'form': form})


# Activating and deactivating users (switching is_active status)
@login_required
def switch_status(request):
    if request.method == 'POST':
        to_be_switched = request.POST.get('name_of_user')
        user = User.objects.get(username=to_be_switched)
        if user.is_active:
            User.objects.filter(username=to_be_switched).update(is_active=False)
        elif not user.is_active:
            User.objects.filter(username=to_be_switched).update(is_active=True)
