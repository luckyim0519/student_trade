from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_page_views, name='start_page_views'),
]