from django.urls import path
from .views import cottage_letter


urlpatterns = [
    path('cottage-page-hello', cottage_letter),
]