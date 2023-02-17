from django.http import HttpResponse
from django.shortcuts import render


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