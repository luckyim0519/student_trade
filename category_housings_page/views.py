from django.http import HttpResponse
from django.shortcuts import render

def category_housings_page_views(request):
    return HttpResponse("This is the category_housings_page")