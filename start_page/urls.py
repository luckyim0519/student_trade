from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_views, name="home_views"),
    #path("", views.start_page_views, name='start_page_views'),
    #path("", views.start_page_views_home, name="start_page_views_home")
]