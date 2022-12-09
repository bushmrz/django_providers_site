from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def Page(request):
    users_list = User.objects.all()
    return render(request, 'temp/UserList.html', locals())