from rest_framework import serializers
from .models import Tracking

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = [
            'tracking_number', 
            'patron_fname', 
            'patron_lname', 
            'id_number', 
            'patron_dept', 
            'patron_type', 
            'request_status', 
            'patron_due_date', 
            'request_book'
        ]
