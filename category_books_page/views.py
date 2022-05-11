from django.http import HttpResponse
from django.shortcuts import render

def category_books_page_views(request):
    return HttpResponse("This is category_books_page")