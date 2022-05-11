from django.http import HttpResponse
from django.shortcuts import render

def category_clothings_page_views(request):
    return HttpResponse("This is the category_clothings_page")