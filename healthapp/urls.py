from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.get_data),
    path('post/', views.get_data)
]