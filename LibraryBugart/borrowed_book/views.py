from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import BorrowedBookSerializer
from .models import BorrowedBook


class BorrowedBookViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BorrowedBookSerializer
    queryset = BorrowedBook.objects.all()

    def get_queryset(self):
        queryset = BorrowedBook.objects.all().order_by('date_added')
        return queryset
