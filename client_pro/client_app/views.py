from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import userDetails

# Create your views here.
def clientAdmin(req):
    return render(req, 'admin.html')

def adminHome(req):
    if req.method == 'POST':
        adminName = req.POST['admin-name']
        adminPassword = req.POST['admin-password']
        try:
            adminUser = User.objects.get(username=adminName)
            adminToken = Token.objects.get(user=adminUser)
            myUser = auth.authenticate(username=adminName, password=adminPassword)
            if myUser is not None:
                req.session['adminId'] = adminUser.username
                auth.login(req, myUser)
                return render(req, 'adminHome.html')
            else:
                context = {'msg' : 'Invalid credential...'}
                print('Invalid credential...')
                return render(req, 'admin.html', context)
        except:
            context = {'msg' : 'You are not registered admin..'}
            print('You are not registered admin..')
            return render(req, 'admin.html', context)
    try:
        if req.session['adminId']:
            return render(req, 'adminHome.html')
    except:
        return HttpResponse("Your session is expire. please Login again")

def adminLogout(req):
    try:
        del req.session['adminId']
        auth.logout(req)
    except:
        return HttpResponse("Your session expire.")
    return render(req, "admin.html")

def index(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        try:
            user = User.objects.get(username=username)
            token = Token.objects.get(user=user)
            myuser = auth.authenticate(username=username, password=password)
            if myuser is not None:
                req.session['userId'] = user.username
                auth.login(req, myuser)
                return render(req, 'home.html')
            else:
                context = {'msg' : 'Invalid credential...'}
                return render(req, 'login.html', context)
        except:
            context = {'msg' : 'You are not registered user..'}
            return render(req, 'shop/login.html', context)
    else:
        return render(req, 'shop/login.html')
