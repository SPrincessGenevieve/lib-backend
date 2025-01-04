from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PatronSerializer
from .models import Patron


class PatronViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PatronSerializer
    queryset = Patron.objects.all()

    def get_queryset(self):
        queryset = Patron.objects.all().order_by('date_added')
        return queryset
