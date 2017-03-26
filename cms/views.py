from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from .forms import MyUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


# Create your views here.
@login_required
def main_list(request):
    """
    Main view which renders the main_list template, filling it with user and company data
    :param request:
    :return: renders the main_list, passing all companies and users
    """
    companies = Company.objects.all().order_by('name')
    users = User.objects.all().order_by('username')
    return render(request, 'cms/main_list.html', {'companies': companies, 'users': users})


@login_required
def company_list(request):
    companies = Company.objects.all().order_by('name')
    return render(request, 'cms/company_list.html', {'companies': companies})


# Adding new companies
@login_required
def add_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            # check if the new company isn't already in our database
            is_repeated = False
            for existing_company in Company.objects.all():
                if company.name == existing_company.name:
                    is_repeated = True
            if is_repeated:
                return render(request, 'cms/company_add.html', {'form': form, 'already_exists': True})
            else:
                company.creator = request.user
                company.save()
                return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'cms/company_add.html', {'form': form, 'already_exists': False})


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
    # test response
    response_data = {'is_ok': True}
    if request.method == 'POST':
        to_be_switched = request.POST.get('name_of_user')
        user = User.objects.get(username=to_be_switched)
        if user.is_active:
            User.objects.filter(username=to_be_switched).update(is_active=False)
        elif not user.is_active:
            User.objects.filter(username=to_be_switched).update(is_active=True)
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
