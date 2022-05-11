from django.http import HttpResponse
from django.shortcuts import render

def category_sports_page_views(request):
    return HttpResponse("This is the category_sports_page")