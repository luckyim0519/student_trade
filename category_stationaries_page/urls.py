from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_stationaries_page_views, name='category_stationaries_page_views'),
]