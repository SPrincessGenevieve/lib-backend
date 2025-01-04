from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Book
        fields = ('book_id', 'book_title', 'book_isbn', 'book_author', 'book_total_copies', 'book_available_copies', 'book_desc', 'book_image', 'category', 'borrowing_period', 'book_date_added')
        read_only_fields = ('book_id', 'book_date_added')
