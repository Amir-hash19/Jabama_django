from django.urls import path
from .views import apartment_letter



urlpatterns = [
    path('apartment-page-hello', apartment_letter),
]
