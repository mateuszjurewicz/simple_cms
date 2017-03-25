from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from .forms import MyUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main_list(request):
    companies = Company.objects.all().order_by('name')
    users = User.objects.all().order_by('username')
    return render(request, 'cms/main_list.html', {'companies': companies, 'users': users})


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
