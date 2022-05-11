from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_tickets_page_views, name='category_tickets_page_views'),
]