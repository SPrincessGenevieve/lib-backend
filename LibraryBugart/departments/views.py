from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import DepartmentSerializer
from .models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        queryset = Department.objects.all().order_by('date_added')
        return queryset