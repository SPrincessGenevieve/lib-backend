from rest_framework import viewsets
from .models import Tracking
from .serializers import TrackingSerializer

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
