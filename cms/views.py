from django.shortcuts import render
from .models import Company

# Create your views here.
def main_list(request):
    # grab all added companies in alphabetical order
    companies = Company.objects.all().order_by('name')
    return render(request, 'cms/main_list.html', {'companies' : companies})