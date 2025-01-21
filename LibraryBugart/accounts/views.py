from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        queryset = Account.objects.all().order_by('creation_date')
        return queryset
