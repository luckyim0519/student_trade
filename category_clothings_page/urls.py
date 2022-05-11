from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_clothings_page_views, name='category_clothings_page_views'),
]