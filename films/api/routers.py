from django.db import router
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from films.api.views import MovieViewSet

router = DefaultRouter()

router.register(r'movies/',MovieViewSet, basename= 'movie')

URLPatterns = router.urls