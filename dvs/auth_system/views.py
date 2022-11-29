from .models import Profile
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .helper import send_forget_password_mail
from django.contrib import messages


def anonymous_required(function=None, redirect_url='home-page'):

   if not redirect_url:
       redirect_url = settings.LOGIN_REDIRECT_URL

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


#Application of the Decorator



@login_required
def HomePage(request):
    return render(request, 'temp/index.html', {

    })

@anonymous_required
def Register(request):
    # CHOICES = (('provider', 'provider'), ('salesman', 'salesman'),)
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # role = request.POST.get('role', None)

        new_user = User.objects.create_user(user_name, email, password)
        new_user.last_name = lname
        new_user.first_name = fname
        new_user.save()

        new_profile = Profile.objects.create(user = new_user)
        new_profile.save()
        
        return redirect('login')

    return render(request, 'temp/sigin.html', {})

@anonymous_required
def Login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        print('ПРОВЕРКА')
        print(user is not None)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Неправильный логин или пароль')

    return render(request, 'temp/login.html', {})


def LogOutUser(request):
    logout(request)
    return redirect('login')


def ChangePassword(request, token):
    context = {}

    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
            
            
    except Exception as e:
        print(e)
    return render(request, 'temp/change-password.html' , context)


import uuid
@anonymous_required
def ForgetPassword(request):
    print('xui')
    try:
        print(request.method)
        if request.method == 'POST':
            print('asdfgh')
            email = request.POST.get('email')
            
            print('nnn')
            
            if not User.objects.filter(email=email).first():
                messages.success(request, 'Not user found with this email.')
                return redirect('forgotPass')
            
            print('aaa')

            user_obj = User.objects.get(email = email)
            print('aaa1')

            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            print('aaa2')
            profile_obj.forget_password_token = token
            profile_obj.save()
            print('aaa33')
            
            print(user_obj.email)
            send_forget_password_mail(user_obj.email, token)
            print('aaa3')
            messages.success(request, 'An email is sent.')
            print('bbb')
            return redirect('forgotPass')

                
        print('xxxxxxxxxx')
    
    except Exception as e:
        print('ошибка в коде :(')
        print(e)
    return render(request, 'temp/forgotPassword.html', {})