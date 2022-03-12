from django.shortcuts import redirect, render, HttpResponse
from .models import userDetails
from flask import request as req

# Create your views here.
def index(req):
    # return HttpResponse("s")
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        print(username,password + " is Registered")
        return redirect('/client/index')
    else:
        return render(req, 'Regist.html')

# from django.shortcuts import render,HttpResponse,redirect
# from rest_framework import viewsets
# from django.contrib import auth
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
# from .models import Profile, ShippingAddress, Product, Cart, Order
# from django.views.generic.list import ListView
# from django.views.generic.base import TemplateView
# from django.views.generic.edit import FormView
# from .forms import Edit_Profile, prof, ship
# from django.contrib.auth.decorators import login_required
# import smtplib

# def index(request):
# 	return render(request, 'shop/index.html')


# def signin(request):
# 	if request.method == "POST":
# 		username = request.POST['name']
# 		password = request.POST['pass']
# 		try:
# 			user = User.objects.get(username=username)
# 			token = Token.objects.get(user=user)
# 			myuser = auth.authenticate(username=username, password=password)
# 			if myuser is not None:
# 				auth.login(request, myuser)
# 				return render(request, 'shop/index.html')
# 			else:
# 				context = {'msg' : 'Invalid credential...'}
# 				return render(request, 'shop/login.html', context)
# 		except:
# 			context = {'msg' : 'You are not registered user..'}
# 			return render(request, 'shop/login.html', context)
# 	else:
# 		return render(request, 'shop/login.html')