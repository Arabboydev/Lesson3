from django.urls import path
from .views import get_info, get_technology, detail


urlpatterns = [
    path('', get_info, name="get_info"),
    path('technology/<int:pk>', get_technology, name="get_technology"),
    path('technology/detail/<int:pk>', detail, name="detail"),
]