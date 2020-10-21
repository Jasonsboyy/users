from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users
# Create your views here.
def func(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.create(username=username,password=password)
        return HttpResponse('注册成功')
