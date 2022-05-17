from django.http import HttpResponse
from django.shortcuts import render

def login_page_views(request):
    return render(request, 'login_page/index.html')