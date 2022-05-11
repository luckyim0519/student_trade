from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_musical_instruments_page_views, name='category_musical_instruments_page_views'),
]