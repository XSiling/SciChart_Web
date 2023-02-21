from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import User


def hello(request):
    return HttpResponse("Hello World!")

def runoob(request):
    import datetime
    now = datetime.datetime.now()
    context = {}
    context['hello'] = ['Hello World ! ', 'Second Hello', 'Third Hello']
    context['time'] = now
    context['number'] = 3
    return render(request, 'runoob.html', context)

def test(request):
    context = {}
    return render(request, 'test.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def line_chart(request):
    context = {}
    return render(request, 'line_chart.html', context)

def histogram(request):
    context = {}
    return render(request, 'histogram.html', context)
    
def mainpage(request):
    
    context = {}
    context['username'] = request.POST.get('fname')
    context['password'] = request.POST.get('pw')

    if 'login' in request.POST:
        print("登录")
        print("A user login, name:", context['username'], "password:", context['password'])
        
        users = User.objects.all()
        for u in users:
            if u.fname == context['username']:
                # there is a user exists.
                if u.pw == context['password']:
                    # login successfully
                    global global_username
                    global_username = context['username']
                    return render(request, 'mainpage.html', context)
                else:
                    context['message'] = '您输入的密码错误'
                    return render(request, 'login.html', context)
        context['message'] = '用户不存在'
        return render(request, 'login.html', context)


    elif 'register' in request.POST:
        print("注册")
        print("A user registers:", context['username'], "password:", context['password'])
        
        if context['username'] == '':
            context['message'] = '用户名需要不为空'
            return render(request, 'login.html', context)
        
        users = User.objects.all()
        for u in users:
            if u.fname == context['username']:
                context['message'] = '该用户名已被注册'
                return render(request, 'login.html', context)
        
        if context['password'] == '':
            context['message'] = '密码需要不为空'
            return render(request, 'login.html', context)

        new_user = User(fname=context['username'], pw=context['password'])
        new_user.save()
        context['message'] = '注册成功'
        return render(request, 'login.html', context)