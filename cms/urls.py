from django.conf.urls import url
from . import views

urlpatterns = [
    # order matters, I had to put the add/new view on top
    url(r'^disable/user/$', views.disable_user, name='disable_user'),
    url(r'^add/user/$', views.add_user, name='add_user'),
    url(r'^add/new/$', views.add_new, name='add_new'),
    url(r'^', views.main_list, name='main_list'),
]
