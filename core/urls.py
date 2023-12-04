from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base),
    path("index/", views.index),
    path('about/', views.about)
]