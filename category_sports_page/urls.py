from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_sports_page_views, name='category_sports_page_views'),
]