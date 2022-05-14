from cgitb import reset
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user) #to check which user is it
    return HttpResponse('<h1>DEFAULT PAGEEE LETS GOOOOOOO</h1>')

def login_page_views(requeest, *args, **kwargs):
    return HttpResponse('<h1>Login page</h1>')

def start_page_views(request):
    return render(request, 'start_page/base.html', {})

def start_page_views_home(request):
    return render(request, "start_page/home.html", {})