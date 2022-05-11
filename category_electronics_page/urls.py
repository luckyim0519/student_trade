from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_electronics_page_views, name='category_electronics_page_views'),
]