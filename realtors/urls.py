from django.urls import path

from . import views

urlpatterns = [
    path('realtor/', views.realtor_view.as_view(), name='realtor-form'),
]
