from rest_framework import serializers
# from rest_framework.parsers import JSONParser
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    serializer for one member record
    """
    class Meta:
        model = Member
        fields = ('id', 'name')


class MemberListSerializer(serializers.ListSerializer):
    """
    serializer for multiple member record
    """
    child = MemberSerializer()
    allow_null = True
    many = True
