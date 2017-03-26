from django.conf.urls import url
from . import views

urlpatterns = [
    # order matters
    url(r'^switch/status/$', views.switch_status, name='switch_status'),
    url(r'^company/list/$', views.company_list, name='company_list'),
    url(r'^add/user/$', views.add_user, name='add_user'),
    url(r'^add/new/$', views.add_new, name='add_new'),
    url(r'^', views.main_list, name='main_list'),
]
