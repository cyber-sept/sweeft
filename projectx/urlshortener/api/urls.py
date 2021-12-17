from django.urls import path, include

from .views import shortener, shortener_premium

urlpatterns = [
    path('short/', shortener, name='shortener'),
    path('short/custom/', shortener_premium, name='premium'),
]
