from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        queryset = Book.objects.all().order_by('date_added')
        return queryset
