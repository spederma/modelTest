# encoding:utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def showUser(request):
    user_list = User.objects.all()
    # print(user_list.query) # 数据库读取出来是queryset
    return render(request, 'index.html', {"userList": user_list})
