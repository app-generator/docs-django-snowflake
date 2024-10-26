# analytics/serializers.py

from rest_framework import serializers

class UserAnalyticsSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=255)
    action = serializers.CharField(max_length=255)
