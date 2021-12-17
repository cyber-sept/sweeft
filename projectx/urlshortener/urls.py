from django.urls import path, include

from .views import home, urlRedirect


urlpatterns = [
    path('', home, name='home'),
    path('<str:slug>', urlRedirect, name='redirect'),
    path('api/', include('urlshortener.api.urls')),
]
