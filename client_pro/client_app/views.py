from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import userDetails, roles

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
                role = userDetails.objects.get(user=adminUser)
                return render(req, 'adminHome.html', {'username': adminName, 'role': role]})
            else:
                context = {'msg' : 'Invalid credential...'}
                print('Invalid credential...')
                return render(req, 'index.html', context)
        except:
            context = {'msg' : 'You are not registered admin..'}
            print('You are not registered admin..')
            return render(req, 'index.html', context)
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
    return redirect('/client/index')

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
        return render(req, 'index.html')

def adminRegister(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['pass']
        email = req.POST['email']
        _roles = req.POST['roles']
        _user = User.objects.create_user(username,email,password)
        _user.save()
        roleDoc = roles.objects.filter(role_id=_roles)
        details = userDetails(user=_user, roles=roleDoc[0])
        details.save()
        return render(req, "adminRegister.html")
    return render(req, 'adminRegister.html')

def verifySuperAdmin(req):
    if req.method == 'POST':
        username = req.POST['super-name']
        password = req.POST['super-password']
        try:
            user = User.objects.get(username=username)
            token = Token.objects.get(user=user)
            myuser = auth.authenticate(username=username, password=password)
            if myuser is not None:
                role = userDetails.objects.get(user=user)
                if role.roles.role_id == '101':
                    return redirect('/client/admin-register')
                context = {'msg' : 'not super head'}
                print(context)
                return render(req, 'verifySuperAdmin.html', context)
            else:
                context = {'msg' : 'Invalid credential...'}
                print(context)                
                return render(req, 'verifySuperAdmin.html', context)
        except:
            context = {'msg' : 'It is not registered user..'}
            print(context)
            return render(req, 'verifySuperAdmin.html', context)
    return render(req, 'verifySuperAdmin.html')
