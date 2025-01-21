from rest_framework import serializers
from .models import Account



class AccountSerializer(serializers.HyperlinkedModelSerializer):
    creation_date = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    class Meta:
        model = Account
        fields = ('account_id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'creation_date', 'password')
        read_only_fields = ('account_id', 'creation_date')
