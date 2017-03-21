from django import forms
from .models. import Company

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('owner', 'name', 'stock_price')