from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main_list(request):
    companies = Company.objects.all().order_by('name')
    users = User.objects.all()
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
