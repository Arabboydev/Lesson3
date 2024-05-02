from django.urls import path
from .views import get_info, get_waters, get_about

urlpatterns = [
    path('', get_info, name="get_info"),
    path('waters/<int:pk>', get_waters, name="get_waters"),
    path('waters/about/<int:pk>', get_about, name="get_about"),
]