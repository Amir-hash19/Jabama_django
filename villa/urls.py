from django.urls import path
from .views import villa_letter



urlpatterns = [
    path('villa-page-hello', villa_letter),
]
