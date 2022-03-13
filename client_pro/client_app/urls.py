from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/index', views.index),
    path('/admin-register', views.adminRegister),
    path('/verify-super', views.verifySuperAdmin),
    path('/admin', views.clientAdmin),
    path('/admin-home', views.adminHome),
    path('/admin-logout', views.adminLogout)
]
