from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page_views, name='main_page_views'),
]