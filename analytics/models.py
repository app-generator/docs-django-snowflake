# analytics/models.py

from django.db import models

class UserAnalytics(models.Model):
    user_id = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
