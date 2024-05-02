from django.urls import path
from .views import get_info, get_student, get_about


urlpatterns = [
    path('', get_info, name="get_info"),
    path('student/<int:pk>', get_student, name="get_student"),
    path('student/about/<int:pk>', get_about, name="get_about"),
]