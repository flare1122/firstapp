# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Grade
from .models import Student


def index(request):
    return HttpResponse("test")


def grade(request):
    gradelist = Grade.objects.all()
    return render(request, 'myapp/grade.html', {"grade": gradelist})


def student(request):
    studentlist = Student.objects.all()
    return render(request, 'myapp/student.html', {"student": studentlist})

def StudentInGrade(request,num):
    grade = Grade.objects.get(pk=num)
    students = grade.student_set.all()
    return render(request,'myapp/student.html',{"student":students})

def login(request):
    # request 包含用户提交的所有信息
    error_msg = ""
    if request.method == 'POST':
    # 获取用户通过post 提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'admin' and pwd == "admin":
            #跳转到响应页面 ("/"相当于前面的地址127.1.0.0:8000)
            return HttpResponse("身份认证成功")
        else:
            #用户名密码不匹配
            return HttpResponse("用户名密码不匹配")
