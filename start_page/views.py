from cgitb import reset
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

def start_page_views(request):
    return render(request, 'start_page/base.html', {})

def start_page_views_home(request):
    return render(request, "start_page/home.html", {})