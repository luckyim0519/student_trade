from django.http import HttpResponse
from django.shortcuts import render

def main_page_views(request):
    return HttpResponse("This is the main_page")