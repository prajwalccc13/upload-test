from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import FlieViewSet


router = routers.DefaultRouter()
router.register('upload', FlieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)