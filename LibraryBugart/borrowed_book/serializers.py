from rest_framework import serializers
from .models import BorrowedBook


class BorrowedBookSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = BorrowedBook
        fields = ('patron', 'book', 'borrow_date', 'due_date')
        read_only_fields = ('borrow_date', 'due_date')
