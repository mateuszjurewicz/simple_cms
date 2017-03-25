"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# for login and logout
from django.contrib.auth import views as auth_views
# for user registration
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('cms.urls'), name='home'),
    # change password
    url('^change-password/$', auth_views.password_change, {'post_change_redirect': 'main_list'},
        name='password_change'),
    # register user
    url('^register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/'), name='register'),
    # login and logout
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'', auth_views.login, name='login'),
]
