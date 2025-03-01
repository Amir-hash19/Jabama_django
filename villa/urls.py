from django.urls import path
from .views import villa_letter



urlpatterns = [
    path('villa-page', villa_letter),
]
