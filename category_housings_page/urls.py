from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_housings_page_views, name='category_housings_page_views'),
]