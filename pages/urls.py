from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='page-home'),
    path('about/', views.about_view, name='page-about'),
]
