from django.shortcuts import render, redirect
from .models import Company

# Create your views here.
def main_list(request):
    if request.user.is_authenticated():
        # grab all added companies in alphabetical order
        companies = Company.objects.all().order_by('name')
        return render(request, 'cms/main_list.html', {'companies': companies})
    else:
        return render(request, 'registration2/login.html')