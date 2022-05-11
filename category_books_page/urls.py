from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_books_page_views, name='category_books_page_views'),
]