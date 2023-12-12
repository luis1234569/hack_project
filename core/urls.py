from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path("index/", views.index),
    path('about/', views.about)
]
