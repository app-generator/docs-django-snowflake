# analytics/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserAnalyticsSerializer
from .models import UserAnalytics

class RecordUserAction(APIView):
    def post(self, request):
        serializer = UserAnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            # Save data to the Snowflake table
            UserAnalytics.objects.create(
                user_id=serializer.validated_data['user_id'],
                action=serializer.validated_data['action']
            )
            return Response({'status': 'success', 'message': 'Data recorded'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
