from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tracking', views.TrackingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
