from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Department
        fields = ('dept_id', 'dept_title', 'date_added')
        read_only_fields = ('dept_id', 'date_added')