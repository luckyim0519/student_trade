from django.http import HttpResponse
from django.shortcuts import render

def category_electronics_page_views(request):
    return HttpResponse("This is the category_electronics_page")