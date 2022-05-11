from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page_views, name='login_page_views'),
]