from django.http import HttpResponse
from django.shortcuts import render

def login_page_views(request):
    return HttpResponse("This is the login_page")