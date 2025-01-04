from rest_framework import serializers
from .models import Patron


class PatronSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Patron
        fields = (
            'request_book', 
            'book_borrowing_period', 
            'patron_id_number', 
            'patron_id', 
            'patron_type', 
            'patron_fname', 
            'patron_lname', 
            'patron_dept', 
            'patron_email', 
            'patron_contact_no', 
            'patron_approved_date', 
            'request_status', 
            'patron_due_date', 
            'date_added',
            'overdue_days'
            )
        read_only_fields = (
            'patron_id', 
            'book_borrowing_period', 
            'patron_approved_date', 
            'patron_due_date', 
            'overdue_days')

