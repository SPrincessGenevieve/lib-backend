from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Category
        fields = ('category_id', 'category_title', 'category_date_added')
        read_only_fields = ('category_id', 'category_date_added')
