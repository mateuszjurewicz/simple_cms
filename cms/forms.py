from django import forms
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# for adding new companies from main list
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('owner', 'name', 'stock_price')


# for adding new users from main list (as opposed to registering when not logged in)
class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super(MyUserForm, self).save(commit=False)

        if commit:
            user.save()

        return user
