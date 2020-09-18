from django.http import HttpResponse
from django.shortcuts import render

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['views_url'] = "<a href='https://www.baidu.com'>baidu</a>"
    return render(request, 'runoob.html', {'views_dict': context})

def hello(request):
    return HttpResponse("Hello world!")
