from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_list, name='main_list'),
]