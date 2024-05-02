from django.urls import path
from .views import get_info, get_products, get_detail

urlpatterns = [
    path('home/', get_info, name="get_name"),
    path('products/<int:pk>', get_products, name="get_products"),
    path('products/detail/<int:pk>', get_detail, name="detail"),
]
