from django.shortcuts import render,redirect
def login(request):
    # request 包含用户提交的所有信息
    error_msg = ""
    if request.method == 'POST':
    # 获取用户通过post 提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        print(pwd,user)
        if user == 'admin' and pwd == "admin":
            #跳转到响应页面 ("/"相当于前面的地址127.1.0.0:8000)
            return redirect('/home')
        else:
            #用户名密码不匹配
            error_msg = "错了 !!!!天啊!!"


    return render(request, 'login.html',{'error_msg':error_msg})